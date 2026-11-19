<?php
/*
 * Ad Pro website chat assistant: the only part of the site that talks to the Claude API.
 * The browser never sees the API key. Answers come only from knowledge.txt, which build.py writes.
 *
 * Raw HTTP (PHP curl) is used instead of the Anthropic PHP SDK because the site is uploaded by hand
 * to Hostinger shared hosting, with no Composer step to install the SDK's vendor folder.
 *
 * API key: put it in ONE of these (first found wins), never in this file or in Git:
 *   1. the ANTHROPIC_API_KEY environment variable
 *   2. adpro-chat-config.php one level ABOVE public_html (safest: not reachable from the web)
 *   3. chat/config.php next to this file
 * Both files look like config.sample.php.
 *
 * GET  -> {"ready": true|false}   (the chat button only appears when ready)
 * POST {"messages":[{"role":"user","content":"..."}, ...]} -> {"reply":"..."}
 */

const MODEL          = 'claude-haiku-5-5';   // cheapest current model; plenty for answering from a fixed set of facts
const EFFORT         = 'low';      // short website answers; raise to 'medium' if answers feel thin
const MAX_TOKENS     = 2000;
const MAX_USER_CHARS = 800;        // longest visitor message accepted
const MAX_MESSAGES   = 16;         // conversation turns sent to the model
const PER_IP_HOUR    = 30;         // messages per visitor per hour
const PER_DAY        = 400;        // messages per day across the whole site (cost ceiling)
const ALLOWED_HOSTS  = ['adproadvertising.in', 'www.adproadvertising.in', 'localhost', '127.0.0.1'];
const HANDOFF        = 'Sorry, I can\'t answer right now. Please message the Ad Pro team on WhatsApp at +91 75609 21593 (https://wa.me/917560921593) or call the same number.';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function out($code, $body)
{
    http_response_code($code);
    echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

function api_key()
{
    $env = getenv('ANTHROPIC_API_KEY');
    if (is_string($env) && trim($env) !== '') return trim($env);
    foreach ([dirname(__DIR__, 2) . '/adpro-chat-config.php', __DIR__ . '/config.php'] as $f) {
        if (is_file($f)) {
            $k = include $f;
            if (is_string($k) && strpos($k, 'sk-ant-') === 0) return trim($k);
        }
    }
    return '';
}

/* Simple file-based limits so one visitor (or a bot) can't run up the bill. */
function within_limits()
{
    $dir = __DIR__ . '/data';
    if (!is_dir($dir) && @mkdir($dir, 0700, true)) @file_put_contents($dir . '/.htaccess', "Require all denied\n");
    if (!is_dir($dir) || !is_writable($dir)) return true;   // never block real visitors because of a disk problem
    $now = time();

    $day = $dir . '/day-' . gmdate('Ymd') . '.txt';
    $h = @fopen($day, 'c+');
    if ($h) {
        flock($h, LOCK_EX);
        $n = (int) stream_get_contents($h);
        if ($n >= PER_DAY) { flock($h, LOCK_UN); fclose($h); return false; }
        ftruncate($h, 0); rewind($h); fwrite($h, (string) ($n + 1));
        flock($h, LOCK_UN); fclose($h);
    }

    $ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'unknown';
    $f = $dir . '/ip-' . substr(hash('sha256', $ip . __DIR__), 0, 24) . '.json';
    $h = @fopen($f, 'c+');
    if ($h) {
        flock($h, LOCK_EX);
        $t = json_decode((string) stream_get_contents($h), true);
        $t = array_values(array_filter(is_array($t) ? $t : [], function ($x) use ($now) { return $x > $now - 3600; }));
        if (count($t) >= PER_IP_HOUR) { flock($h, LOCK_UN); fclose($h); return false; }
        $t[] = $now;
        ftruncate($h, 0); rewind($h); fwrite($h, json_encode($t));
        flock($h, LOCK_UN); fclose($h);
    }

    if (mt_rand(1, 50) === 1) {   // tidy old counters now and then
        foreach (glob($dir . '/*') ?: [] as $old) {
            if (filemtime($old) < $now - 2 * 86400) @unlink($old);
        }
    }
    return true;
}

function host_of($url)
{
    $h = parse_url((string) $url, PHP_URL_HOST);
    return is_string($h) ? strtolower($h) : '';
}

/* ---------- GET: is the assistant switched on? ---------- */
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    out(200, ['ready' => api_key() !== '' && function_exists('curl_init') && is_file(__DIR__ . '/knowledge.txt')]);
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') out(405, ['error' => 'method']);

/* ---------- only from our own pages ---------- */
$from = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : (isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '');
if (!in_array(host_of($from), ALLOWED_HOSTS, true)) out(403, ['error' => 'origin']);

$key = api_key();
if ($key === '' || !function_exists('curl_init')) out(503, ['error' => 'off', 'reply' => HANDOFF]);

/* ---------- read and clean the conversation ---------- */
$in = json_decode((string) file_get_contents('php://input', false, null, 0, 200000), true);
$raw = (is_array($in) && isset($in['messages']) && is_array($in['messages'])) ? $in['messages'] : [];
$msgs = [];
foreach ($raw as $m) {
    if (!is_array($m) || !isset($m['role'], $m['content']) || !is_string($m['content'])) continue;
    $role = $m['role'] === 'assistant' ? 'assistant' : 'user';
    $text = trim(preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $m['content']));
    if ($text === '') continue;
    $limit = $role === 'user' ? MAX_USER_CHARS : 3000;
    if (mb_strlen($text) > $limit) $text = mb_substr($text, 0, $limit);
    if ($msgs && end($msgs)['role'] === $role) {          // keep turns alternating
        $msgs[count($msgs) - 1]['content'] .= "\n\n" . $text;
    } else {
        $msgs[] = ['role' => $role, 'content' => $text];
    }
}
$msgs = array_slice($msgs, -MAX_MESSAGES);
while ($msgs && $msgs[0]['role'] !== 'user') array_shift($msgs);
if (!$msgs || end($msgs)['role'] !== 'user') out(400, ['error' => 'empty']);

if (!within_limits()) {
    out(429, ['error' => 'limit', 'reply' => 'I\'ve answered a lot of messages for now. Please continue with the Ad Pro team on WhatsApp at +91 75609 21593 (https://wa.me/917560921593).']);
}

/* ---------- ask Claude ---------- */
$tz = new DateTimeZone('Asia/Kolkata');
$now = new DateTime('now', $tz);
$payload = [
    'model'         => MODEL,
    'max_tokens'    => MAX_TOKENS,
    'output_config' => ['effort' => EFFORT],
    'system'        => [
        // The large, unchanging knowledge block is cached, so follow-up messages cost far less.
        ['type' => 'text', 'text' => file_get_contents(__DIR__ . '/knowledge.txt'), 'cache_control' => ['type' => 'ephemeral']],
        ['type' => 'text', 'text' => 'Current date and time in Kerala: ' . $now->format('l j F Y, g:i a') . '.'],
    ],
    'messages'      => $msgs,
];

$ch = curl_init('https://api.anthropic.com/v1/messages');
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_TIMEOUT        => 60,
    CURLOPT_HTTPHEADER     => [
        'content-type: application/json',
        'x-api-key: ' . $key,
        'anthropic-version: 2026-10-21',
    ],
    CURLOPT_POSTFIELDS     => json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
]);
$body = curl_exec($ch);
$status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
$cerr = curl_error($ch);
curl_close($ch);

$res = is_string($body) ? json_decode($body, true) : null;
if ($status !== 200 || !is_array($res)) {
    $type = (is_array($res) && isset($res['error']['type'])) ? $res['error']['type'] : ($cerr ?: 'unknown');
    error_log("adpro chat: HTTP $status $type");                // no visitor text in the log
    out(502, ['error' => 'upstream', 'reply' => HANDOFF]);
}

if (isset($res['stop_reason']) && $res['stop_reason'] === 'refusal') {
    out(200, ['reply' => 'I can\'t help with that here. For anything about your business, the Ad Pro team is on WhatsApp at +91 75609 21593 (https://wa.me/917560921593).']);
}

$reply = '';
foreach (isset($res['content']) && is_array($res['content']) ? $res['content'] : [] as $block) {
    if (isset($block['type'], $block['text']) && $block['type'] === 'text') $reply .= $block['text'];
}
$reply = trim($reply);
out(200, ['reply' => $reply !== '' ? $reply : HANDOFF]);
