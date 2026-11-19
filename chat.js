/* Ad Pro website chat assistant. The button only appears when /chat/api.php says the assistant is switched on. */
(function () {
  var API = "/chat/api.php", KEY = "apchat", WA = "https://wa.me/917560921593";
  var ss = { get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
             set: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} } };
  var msgs = [];
  try { msgs = JSON.parse(ss.get(KEY) || "[]") || []; } catch (e) { msgs = []; }
  var busy = false, root, log, form, input, sendBtn, chips;

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  // Plain text in, safe nodes out: links for web addresses, line breaks kept.
  function render(text, into) {
    var re = /(https?:\/\/[^\s<>"')]+[^\s<>"').,;:!?])/g, last = 0, m;
    var lines = String(text).split("\n");
    lines.forEach(function (line, i) {
      if (i) into.appendChild(document.createElement("br"));
      last = 0; re.lastIndex = 0;
      while ((m = re.exec(line))) {
        if (m.index > last) into.appendChild(document.createTextNode(line.slice(last, m.index)));
        var a = el("a", null, m[1].replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""));
        a.href = m[1];
        if (!/^https:\/\/(www\.)?adproadvertising\.in(\/|$)/.test(m[1])) { a.target = "_blank"; a.rel = "noopener"; }
        into.appendChild(a);
        last = m.index + m[1].length;
      }
      if (last < line.length) into.appendChild(document.createTextNode(line.slice(last)));
    });
  }

  function bubble(role, text) {
    var b = el("div", "apc-m " + (role === "user" ? "apc-u" : "apc-a"));
    render(text, b);
    log.appendChild(b);
    log.scrollTop = log.scrollHeight;
    return b;
  }

  function save() { ss.set(KEY, JSON.stringify(msgs.slice(-30))); }

  function waLink() {
    var lastQ = "";
    for (var i = msgs.length - 1; i >= 0; i--) if (msgs[i].role === "user") { lastQ = msgs[i].content; break; }
    var t = "Hello Ad Pro, I was chatting with your website assistant." + (lastQ ? " My question: " + lastQ.slice(0, 300) : "");
    return WA + "?text=" + encodeURIComponent(t);
  }

  function setBusy(on) {
    busy = on;
    sendBtn.disabled = on;
    root.querySelector(".apc-log").setAttribute("aria-busy", on ? "true" : "false");
  }

  function send(text) {
    text = (text || "").trim();
    if (!text || busy) return;
    if (chips) { chips.remove(); chips = null; }
    msgs.push({ role: "user", content: text.slice(0, 800) });
    save();
    bubble("user", text);
    input.value = "";
    autosize();
    setBusy(true);
    var dots = el("div", "apc-m apc-a apc-dots");
    dots.setAttribute("aria-label", "Assistant is typing");
    dots.appendChild(el("i")); dots.appendChild(el("i")); dots.appendChild(el("i"));
    log.appendChild(dots); log.scrollTop = log.scrollHeight;

    fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ messages: msgs.slice(-16) }) })
      .then(function (r) { return r.json().catch(function () { return {}; }); })
      .then(function (d) { return d && d.reply ? d.reply : null; }, function () { return null; })
      .then(function (reply) {
        dots.remove();
        var ok = !!reply;
        reply = reply || "Sorry, I couldn't connect just now. Please message the Ad Pro team on WhatsApp at +91 75609 21593 (" + WA + ").";
        if (ok) { msgs.push({ role: "assistant", content: reply }); save(); }
        bubble("assistant", reply);
        root.querySelector(".apc-wa").href = waLink();
        setBusy(false);
        input.focus();
      });
  }

  function autosize() { input.style.height = "auto"; input.style.height = Math.min(input.scrollHeight, 120) + "px"; }

  function build() {
    root = el("div", "apc");
    root.innerHTML =
      '<button class="apc-open" type="button" aria-expanded="false" aria-controls="apc-panel">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm3 6.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/></svg>' +
        '<span>Ask Ad Pro</span></button>' +
      '<section class="apc-panel" id="apc-panel" role="dialog" aria-label="Chat with the Ad Pro assistant" hidden>' +
        '<header class="apc-hd"><div><b>Ask Ad Pro</b><small>AI assistant. The team is on WhatsApp.</small></div>' +
          '<button class="apc-x" type="button" aria-label="Close chat"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button></header>' +
        '<div class="apc-log" role="log" aria-live="polite" aria-busy="false"></div>' +
        '<form class="apc-f"><label class="apc-sr" for="apc-in">Your question</label>' +
          '<textarea id="apc-in" rows="1" maxlength="800" placeholder="Ask about websites, ads, apps…" autocomplete="off"></textarea>' +
          '<button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button></form>' +
        '<p class="apc-note">AI answers can be wrong, so please don\'t share personal details here. ' +
          '<a class="apc-wa" target="_blank" rel="noopener">Continue on WhatsApp</a></p>' +
      '</section>';
    document.body.appendChild(root);
    document.documentElement.classList.add("has-apc");

    var openBtn = root.querySelector(".apc-open"), panel = root.querySelector(".apc-panel");
    log = root.querySelector(".apc-log"); form = root.querySelector(".apc-f");
    input = root.querySelector("textarea"); sendBtn = form.querySelector("button");
    root.querySelector(".apc-wa").href = waLink();

    bubble("assistant", "Hi! I'm Ad Pro Advertising's AI assistant. Ask me about websites, ads, posters, social media, automation or apps, in English or Malayalam.");
    if (msgs.length) msgs.forEach(function (m) { bubble(m.role, m.content); });
    else {
      chips = el("div", "apc-chips");
      ["What services do you offer?", "How much does a website cost?", "Can you help my clinic get more patients?", "Where is your office?"].forEach(function (q) {
        var c = el("button", null, q); c.type = "button";
        c.addEventListener("click", function () { send(q); });
        chips.appendChild(c);
      });
      log.appendChild(chips);
    }

    function open(on) {
      panel.hidden = !on;
      openBtn.setAttribute("aria-expanded", on ? "true" : "false");
      root.classList.toggle("on", on);
      if (on) { log.scrollTop = log.scrollHeight; setTimeout(function () { input.focus(); }, 30); }
      else openBtn.focus();
      ss.set(KEY + "-open", on ? "1" : "");
    }
    openBtn.addEventListener("click", function () { open(panel.hidden); });
    root.querySelector(".apc-x").addEventListener("click", function () { open(false); });
    root.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) open(false); });
    form.addEventListener("submit", function (e) { e.preventDefault(); send(input.value); });
    input.addEventListener("input", autosize);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey && !e.isComposing) { e.preventDefault(); send(input.value); }
    });
    if (ss.get(KEY + "-open") && window.innerWidth > 600) open(true);
  }

  function start() {
    var cached = ss.get(KEY + "-ready");
    if (cached === "1") return build();
    if (cached === "0") return;
    fetch(API, { headers: { Accept: "application/json" } })
      .then(function (r) { return r.ok ? r.json() : { ready: false }; })
      .then(function (d) { var on = !!(d && d.ready); ss.set(KEY + "-ready", on ? "1" : "0"); if (on) build(); })
      .catch(function () {});
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
