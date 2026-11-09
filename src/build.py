"""Ad Pro Advertising website generator (v2, Nov 2026). Run: python3 build.py -> dist/"""
import os, json, shutil, html
SITE = "https://adproadvertising.in"
WA = "917560921593"
PHONE = "75609 21593"
TEL = "+917560921593"
OUT = "dist"
YEAR = 2026

def wa(msg="Hello Ad Pro, I'd like to discuss a project."):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

WA_ICON = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.6 5.8 5 2.1.9 3 1 4 .8.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.3.2-1.5-.1-.1-.3-.2-.6-.3z"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
PHONE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
MENU_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h12"/></svg>'

# the two hands from the logo (same geometry as the master artwork)
HB = "M927 298 1200 25 590 25 117 498 294.5 473 394.5 373Z"
HR = "M1158 218 1001.5 240 921.5 320 452 386 227 611 765 611Z"
def hands_svg(cls="", label=False):
    return (f'<svg class="{cls}" viewBox="100 10 1080 615" aria-hidden="true" focusable="false">'
            f'<path class="hb" fill="#4BA4F4" d="{HB}"/><path class="hr" fill="#E73A2A" d="{HR}"/></svg>')

SERVICES = [
    ("website-design-local-seo.html", "Websites & Local SEO", "Websites",
     "Fast hand-coded websites with the full local SEO package, so people searching nearby find you first."),
    ("meta-google-ads.html", "Meta & Google Ads", "Ads",
     "Facebook, Instagram and Google campaigns judged on real enquiries, not likes."),
    ("posters-video-ads.html", "Posters & Video Ads", "Posters & video",
     "Posters, social creatives and short reels in Malayalam and English, sized for every placement."),
    ("app-development.html", "App Development", "Apps",
     "Android, iPhone, web and Windows apps, built around how your staff already work."),
]

CASES = [
    dict(id="gtec", img="work-gtec.jpg", url="https://gteccharummood.in", host="gteccharummood.in",
         kind="Computer training centre, Charummood, Alappuzha", client="G-TEC Computer Education, Charummood",
         title="One training centre, every channel: website, ads, video, WhatsApp automation and a lobby TV app.",
         tags=["Website", "Local SEO", "Meta Ads", "Video", "App"],
         short=["28 pages rebuilt by hand. 21 kept their exact address and the rest were redirected, so existing Google rankings carried over.",
                "Enquiry form that records which ad the lead came from, then opens WhatsApp."],
         full=["Replaced a page-builder site with a hand-coded static site and kept all 28 existing pages. 21 kept their exact URL and the rest were permanently redirected, so the rankings the centre already had carried over.",
               "Course pages with GST-inclusive fees, LocalBusiness and Course structured data, and an enquiry form that records the ad lead, then opens WhatsApp.",
               "A built-in enquiry assistant that answers course and fee questions on the page itself.",
               "Facebook and Instagram campaigns checked daily against the centre's own enquiry sheet, plus Google Business Profile posts.",
               "15-second motion-graphics reels with Malayalam text and a Malayalam female voice-over, in offer and evergreen versions.",
               "A WhatsApp Business Cloud API auto-reply engine that quotes exactly the same fees as the website and goes quiet when staff reply by hand.",
               'The lobby TV attendance app that became <a href="batchboard.html">BatchBoard</a>.']),
    dict(id="hannah", img="work-hannah.jpg", url="https://hannahhomecare.in", host="hannahhomecare.in",
         kind="Home nursing and elderly care, Bengaluru", client="Hannah Home Care and Rehabilitation Centre",
         title="A 21-page rebuild for a Bengaluru home-care company, moved onto its own domain.",
         tags=["Website", "Local SEO", "Branding"],
         short=["A page for every service, from home nursing procedures to baby care and hospital attenders.",
                "Eight Bengaluru locality pages and a guide for families arranging care from abroad."],
         full=["Replaced a page-builder site with a 21-page hand-coded site on hannahhomecare.in, with HTTPS and redirects from the old addresses.",
               "Separate pages for each service: home nursing (with the full list of procedures done at home), elderly care and attendants, physiotherapy, stroke and neuro rehab, post-surgical care, and baby care with nannies, house maids and hospital attenders.",
               "Eight Bengaluru locality pages, a page explaining what home care costs, and a guide for families arranging care from abroad.",
               "Rebranded to the client's logo, with the Koramangala office, both managing directors and direct lines, a floating WhatsApp button, and home-health structured data.",
               "Google Search Console set up on the domain through DNS, ready for the sitemap."]),
    dict(id="sg", img="work-sg.jpg", url="https://lavender-spider-339191.hostingersite.com", host="S&G Polymers preview site",
         kind="PET bottle manufacturer, Punnapara, Alappuzha", client="S&G Polymers",
         title="A 16-page manufacturer site built to win bulk orders from across Kerala.",
         tags=["Website", "Local SEO"],
         short=["Product pages for the 20 litre jar, 1 litre and 500 ml bottles.",
                "A Kerala delivery page plus six district pages, so buyers searching nearby find a page written for their area."],
         full=["Replaced a page-builder template with a 16-page hand-coded site.",
               "Product pages for the 20 litre jar, 1 litre and 500 ml bottles, with Product structured data.",
               "A Kerala delivery page plus six district pages (Alappuzha, Cherthala, Kayamkulam, Kollam, Kottayam, Ernakulam), so buyers searching nearby find a page written for their area.",
               "A quote form that writes the order details into WhatsApp, and logo lockups cut cleanly from the client's own artwork."]),
]

INCLUDES = ["On-page and technical SEO", "LocalBusiness and Service schema", "Google Business Profile set-up",
            "Same name, address and phone everywhere", "Local citations and a review plan", "Search Console and Analytics 4",
            "Locality and service pages", "WhatsApp enquiry forms"]

STEPS = [("Talk", "A short call or WhatsApp chat about what you sell, who buys it and where they are."),
         ("Plan", "We list the pages, campaigns or app screens and agree them with you before building anything."),
         ("Build", "Code, copy, design and video are all made in-house. You review everything on a preview link first."),
         ("Launch and measure", "We go live, connect Search Console, Analytics and your ad accounts, and check that enquiries actually arrive.")]

# ---------------- shared chrome ----------------
def head(title, desc, path, extra_ld=None):
    url = SITE + "/" + ("" if path == "index.html" else path)
    org = {"@type": "ProfessionalService", "@id": SITE + "/#org", "name": "Ad Pro Advertising", "url": SITE + "/",
           "logo": SITE + "/logo.png", "image": SITE + "/og-image.jpg", "telephone": TEL,
           "slogan": "Websites, ads and apps that bring in enquiries",
           "address": {"@type": "PostalAddress", "addressLocality": "Charummood", "addressRegion": "Kerala", "addressCountry": "IN"},
           "areaServed": [{"@type": "State", "name": "Kerala"}, {"@type": "Country", "name": "India"}],
           "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[1], "url": f"{SITE}/{s[0]}"}} for s in SERVICES],
           "knowsLanguage": ["en", "ml"], "sameAs": ["https://www.instagram.com/adpro_advt/"]}
    graph = [org, {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Ad Pro Advertising", "publisher": {"@id": SITE + "/#org"}}]
    if extra_ld: graph += extra_ld
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    t, d = html.escape(title), html.escape(desc)
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0D0D0D">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/archivo-x.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/jakarta.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website"><meta property="og:site_name" content="Ad Pro Advertising">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{ld}</script>
<link rel="stylesheet" href="site.css?v=2">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(cur):
    def a(href, label):
        c = ' aria-current="page"' if href == cur else ""
        return f'<a href="{href}"{c}>{label}</a>'
    dd = "".join(f'<a href="{s[0]}"><b>{html.escape(s[1])}</b><span>{html.escape(s[3].split(",")[0].split(".")[0])}</span></a>' for s in SERVICES)
    dd += '<a href="batchboard.html"><b>BatchBoard</b><span>Lobby TV attendance app for training centres</span></a>'
    svc_cur = ' aria-current="page"' if cur in [s[0] for s in SERVICES] else ""
    return f'''<header class="hd"><div class="wrap">
<a class="brand" href="index.html" aria-label="Ad Pro Advertising, home"><img src="logo.svg" width="168" height="80" alt="Ad Pro Digital Marketing"></a>
<button class="menu" aria-expanded="false" aria-controls="nav" aria-label="Open menu">{MENU_ICON}</button>
<nav class="nav" id="nav" aria-label="Main">
<div class="dd"><button type="button" aria-expanded="false"{svc_cur}>Services {CHEV}</button><div class="dd-panel">{dd}</div></div>
{a("work.html","Our work")}{a("batchboard.html","BatchBoard")}{a("about.html","About")}{a("contact.html","Contact")}
</nav>
<a class="btn btn-ink" href="{wa()}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a>
</div></header>
<main id="main">
'''

def cta(h="Tell us what you sell and who buys it.", p="We'll tell you what would bring you more enquiries: a website, ads, creatives or an app. No obligation."):
    return f'''<section class="cta">{hands_svg("cs")}<div class="wrap">
<div><h2 class="d2">{h}</h2><p>{p}</p></div>
<div class="acts"><a class="call" href="tel:{TEL}"><small>Call or WhatsApp</small><span class="num">{PHONE}</span></a>
<a class="btn btn-sky" href="{wa()}" target="_blank" rel="noopener">{WA_ICON} Chat on WhatsApp</a></div>
</div></section>
'''

def footer():
    svc = "".join(f'<li><a href="{s[0]}">{html.escape(s[1])}</a></li>' for s in SERVICES) + '<li><a href="batchboard.html">BatchBoard</a></li>'
    return f'''</main>
<footer class="ft"><div class="wrap">
<div class="cols">
<div><a href="index.html" aria-label="Ad Pro Advertising, home"><img src="logo-reverse.svg" width="180" height="85" alt="Ad Pro Digital Marketing"></a>
<p>Websites, local SEO, ads, posters, video and apps for businesses in Charummood, across Kerala and beyond.</p>
<p>Charummood, Alappuzha, Kerala</p></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Contact</h3><ul>
<li>Call or WhatsApp<br><a class="num" href="tel:{TEL}" style="color:#fff;font-size:1.3rem">{PHONE}</a></li>
<li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp us</a></li>
<li><a href="work.html">Our work</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li>
<li><a href="https://www.instagram.com/adpro_advt/" target="_blank" rel="noopener">Instagram @adpro_advt</a></li></ul></div>
</div>
<div class="base"><span>&copy; {YEAR} Ad Pro Advertising, Charummood. All rights reserved.</span><span>Charummood, Alappuzha</span></div>
</div></footer>
<a class="wafab" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat with Ad Pro on WhatsApp">{WA_ICON}</a>
<nav class="mbar" aria-label="Quick contact"><a class="c" href="tel:{TEL}"><small>Call or WhatsApp</small><span class="num">{PHONE}</span></a><a class="w" href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp Ad Pro">{WA_ICON}</a></nav>
<script>
(function(){{var b=document.querySelector('.menu'),n=document.getElementById('nav');
if(b)b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
document.querySelectorAll('.dd>button').forEach(function(x){{x.addEventListener('click',function(){{var o=x.parentNode.classList.toggle('open');x.setAttribute('aria-expanded',o)}})}});
var h=document.querySelector('.hd');var s=function(){{h.classList.toggle('scrolled',window.scrollY>8)}};window.addEventListener('scroll',s,{{passive:true}});s();
var f=document.getElementById('qf');if(f)f.addEventListener('submit',function(e){{e.preventDefault();var g=function(i){{var x=document.getElementById(i);return x?x.value.trim():''}};
var m='Hello Ad Pro,\\n\\nName: '+g('n')+'\\nBusiness: '+g('b')+'\\nPlace: '+g('p')+'\\nNeed: '+g('s')+'\\n\\n'+g('m');
window.open('https://wa.me/{WA}?text='+encodeURIComponent(m),'_blank','noopener')}});}})();
</script>
</body>
</html>
'''

def page(path, title, desc, body, extra_ld=None):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, path), "w").write(head(title, desc, path, extra_ld) + header(path) + body + footer())

def chips(tags, cls=""):
    return f'<ul class="chips {cls}">' + "".join(f"<li>{t}</li>" for t in tags) + "</ul>"

def case_html(c, i, full=False):
    pts = c["full"] if full else c["short"]
    li = "".join(f"<li>{p}</li>" for p in pts)
    flip = " flip" if i % 2 else ""
    return f'''<article class="case{flip}" id="{c["id"]}">
<a class="shot" href="{c["url"]}" target="_blank" rel="noopener" aria-label="Open the {html.escape(c["client"])} website"><span class="bar"><i></i><i></i>{html.escape(c["host"])}</span><img src="{c["img"]}" width="960" height="426" loading="lazy" alt="Home page of the {html.escape(c["client"])} website, built by Ad Pro"></a>
<div><div class="kind">{html.escape(c["kind"])}</div><h3 class="d3">{html.escape(c["client"])}</h3><p>{html.escape(c["title"])}</p>
{chips(c["tags"])}<div class="prose" style="color:#cfd5db"><ul>{li}</ul></div>
<a class="link" href="{c["url"]}" target="_blank" rel="noopener">Visit the live site</a></div>
</article>'''

def faq_ld(qs):
    return [{"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}]

def crumbs_ld(name, path):
    return [{"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}/{path}"}]}]

def inner(path, name, h1, lede, sections, faqs, wa_msg, side_title="Talk to us about this",
          side_text="Tell us about your business on WhatsApp. We reply with what we would do and a quote.", price=None, title=None, desc=None):
    others = "".join(f'<li><a href="{s[0]}">{html.escape(s[1])}</a></li>' for s in SERVICES if s[0] != path)
    if path != "batchboard.html": others += '<li><a href="batchboard.html">BatchBoard</a></li>'
    secs = "".join(f"<section><h2>{h}</h2>{b}</section>" for h, b in sections)
    pr = f'<span class="price">{price}</span>' if price else ""
    fq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faqs)
    body = f'''<section class="ph">{hands_svg("cs")}<div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / {html.escape(name)}</div>
<h1 class="d1">{h1}</h1>{pr}<p class="lede">{lede}</p></div></section>
<section class="sec"><div class="wrap"><div class="layout"><div class="prose">{secs}</div>
<aside class="side"><div class="box dark"><h3>{side_title}</h3><p>{side_text}</p>
<a class="btn btn-sky" href="{wa(wa_msg)}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a>
<a class="btn btn-ghost" href="tel:{TEL}">{PHONE_ICON} Call <span class="num">{PHONE}</span></a></div>
<div class="box"><h3>Other services</h3><ul>{others}</ul></div></aside></div></div></section>
<section class="sec mist"><div class="wrap"><div class="sec-h"><h2 class="d2">Questions</h2></div><div class="faq">{fq}</div></div></section>
{cta()}'''
    page(path, title or f"{name} | Ad Pro Advertising, Alappuzha", desc or lede, body, faq_ld(faqs) + crumbs_ld(name, path))

def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

# ---------------- HOME ----------------
svc_rows = "".join(f'<a href="{s[0]}"><span class="d3">{html.escape(s[1])}</span><p>{html.escape(s[3])}</p><span class="go">{ARROW}</span></a>' for s in SERVICES)
svc_rows += f'<a href="batchboard.html"><span class="d3">BatchBoard<span class="tagp">Product</span></span><p>Live batch attendance on your lobby TV, with your ads in between. &#8377;5,000 one-time.</p><span class="go">{ARROW}</span></a>'
proof = "".join(f'<a href="#{c["id"]}"><b>{html.escape(c["client"].split(",")[0].replace(" and Rehabilitation Centre",""))}</b><span>{html.escape(c["host"] if "." in c["host"] else "Live preview site")}</span></a>' for c in CASES)
home = f'''<section class="hero"><div class="wrap hero-grid">
<div><p class="where"><i></i>Digital marketing studio in Charummood, Alappuzha</p>
<h1 class="d1">Websites, ads and apps that bring in enquiries.</h1>
<p class="lede">We build fast websites that rank locally, run Facebook, Instagram and Google ads measured on real leads, design posters and Malayalam reels, and develop apps. All in-house, all for one result: more of the right people calling you.</p>
<div class="ctas"><a class="btn btn-ink" href="{wa()}" target="_blank" rel="noopener">{WA_ICON} Chat on WhatsApp</a><a class="btn btn-line" href="work.html">See our work</a></div></div>
<div class="hands">{hands_svg()}</div>
</div>
<div class="proof"><div class="wrap"><span class="lab">Live client work</span>{proof}</div></div>
</section>

<section class="sec"><div class="wrap">
<div class="sec-h"><h2 class="d2">One team for the whole job.</h2><p>The website, the ads that send people to it, the creatives inside those ads, and the app behind them. One team answers for the result.</p></div>
<nav class="svc" aria-label="Services">{svc_rows}</nav>
</div></section>

<section class="sec ink"><div class="wrap">
<div class="sec-h"><h2 class="d2">Recent work. All live, open them and judge.</h2><p>A training centre in Charummood, a home-care company in Bengaluru and a bottle manufacturer in Alappuzha.</p></div>
{"".join(case_html(c, i) for i, c in enumerate(CASES))}
<p style="margin-top:40px"><a class="btn btn-sky" href="work.html">Read the full case studies {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split">
<div><h2 class="d2">Every website ships with the full local SEO package.</h2><p class="lede">Not an upgrade or a monthly add-on. A website nobody finds on Google doesn't bring in enquiries, so this is part of every site we deliver.</p>
<a class="link" href="website-design-local-seo.html">How our websites work</a></div>
<ul class="ticks">{"".join(f"<li>{i}</li>" for i in INCLUDES)}</ul>
</div></section>

<section class="sec mist"><div class="wrap">
<div class="sec-h"><h2 class="d2">How a project runs</h2><p>Four steps, and nothing goes live without your approval.</p></div>
<ol class="steps">{"".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in STEPS)}</ol>
</div></section>

<section class="sec"><div class="wrap prod">
<div><span class="price">&#8377;5,000 one-time</span><h2 class="d2" style="margin-bottom:18px">BatchBoard: attendance, live on your centre TV.</h2>
<p class="lede">Tutors mark attendance on their phone and the lobby TV shows each batch live. Between batches it plays your ads. Built for training and coaching centres, no subscription.</p>
<a class="btn btn-ink" href="batchboard.html">See how BatchBoard works {ARROW}</a></div>
<div class="tv" aria-hidden="true"><div class="t"><b>Batch C, 10:00</b><span>8 in, 1 on leave, 3 to arrive</span></div>
<div class="g"><span>Anu R.</span><span>Rahul K.</span><span>Sneha M.</span><span class="l">Arjun P. leave</span><span>Fathima S.</span><span>Vishnu T.</span><span class="w">Nikhil A.</span><span>Devika B.</span><span>Aswin J.</span><span class="w">Meera L.</span><span>Sanjay V.</span><span class="w">Ann M.</span></div></div>
</div></section>
{cta()}'''
page("index.html", "Ad Pro Advertising | Websites, SEO, Ads & Apps, Alappuzha",
     "Ad Pro Advertising, Charummood, Alappuzha: hand-coded websites with local SEO, Meta & Google ads, posters, Malayalam video reels and app development.", home)

# ---------------- SERVICE PAGES ----------------
inner("website-design-local-seo.html", "Websites & Local SEO", "Get found on Google by customers nearby.",
      "Hand-coded, fast-loading business websites built to be found on Google, not just to look nice.",
      [("Why hand-coded, not a page builder", "<p>Most small-business sites in Kerala are drag-and-drop builder templates. They load slowly on mobile data, every business looks the same, and the SEO settings are shallow. We write every page by hand as plain, static HTML.</p>" +
        ul(["<b>Loads fast on 4G</b>: no page-builder scripts, no plugins.", "<b>Nothing to hack or update</b>: there is no WordPress admin or plugin to patch.",
            "<b>Cheap to host</b>: a whole site is usually around a megabyte.", "<b>Every page written for a search</b>: its own title, description and structured data."])),
       ("What comes with every website", "<p>Local SEO is not an add-on. Every site we deliver ships with the same package:</p>" +
        ul(["On-page and technical SEO: titles, descriptions, headings, sitemap, robots, redirects, HTTPS", "Schema.org structured data: LocalBusiness, Service or Product, FAQ, breadcrumbs",
            "Google Business Profile setup or clean-up", "NAP consistency: your name, address and phone the same everywhere", "Local citations and a review strategy",
            "Google Search Console and Google Analytics 4 connected", "WhatsApp enquiry button and forms that open a ready-written WhatsApp message"])),
       ("Locality and service pages", "<p>People search for <i>“home nurse in Koramangala”</i> or <i>“water bottle supplier Kottayam”</i>, not for your company name. So we build a page for each service you sell and each area you cover, each written for that search, so you can show up for it.</p>"),
       ("Moving from an old site without losing Google", "<p>If you already have a site that ranks, we list every existing address before touching anything. Pages keep their URL wherever possible and the rest get permanent (301) redirects, so the rankings you have already earned carry over.</p>")],
      [("Can you rebuild my existing website?", "Yes. We pull your current sitemap first, keep the addresses that already rank, and redirect the rest, so a rebuild doesn't reset your Google position."),
       ("Do I need WordPress?", "No. Our sites are static HTML, so there's no WordPress admin, plugin updates or database to maintain. Content changes are made by us and re-uploaded."),
       ("Will my business show on Google Maps?", "We set up or clean up your Google Business Profile and keep your name, address and phone identical across the site and listings. That consistency is what Maps ranking relies on."),
       ("Where is the website hosted?", "On fast shared hosting with free SSL. We can use your existing hosting and domain, or arrange new ones for you.")],
      "Hello Ad Pro, I'm interested in Websites & Local SEO.")

inner("meta-google-ads.html", "Meta & Google Ads", "Ads measured on enquiries, not likes.",
      "Facebook, Instagram and Google campaigns run for real enquiries, and checked against the leads you actually get.",
      [("A conversation is not a customer", "<p>A cheap “conversation started” is not a customer. We keep a simple enquiry sheet with your front office (who enquired, from which ad, what happened next) and compare ad spend against it. Then we can see which ads bring people who actually buy.</p>"),
       ("What we handle", ul(["Campaign set-up on Facebook and Instagram: WhatsApp-conversation, lead and awareness objectives", "Google Ads search campaigns for people already looking for what you sell",
            "Audience and location targeting around your actual catchment", 'Creatives: posters, carousels and video reels made in-house (see <a href="posters-video-ads.html">Posters &amp; Video</a>)',
            "Offer campaigns switched on and off on time, so expired offers don't keep running", "Google Business Profile posts scheduled alongside the ads"])),
       ("Daily checks, honest reporting", "<p>We check spend and results every day and report what changed: spend pace against your monthly ceiling, cost per enquiry, and anything that needs a decision. No change to your budget or campaigns is made without your approval.</p>"),
       ("Small budgets, read carefully", "<p>At a few enquiries a week, one good or bad week means very little. We wait for a consistent pattern before cutting a platform or audience, rather than reacting to noise.</p>")],
      [("Do you need access to my ad account?", "Yes, as a partner on your Meta Business account or Google Ads account. The account and its payment method stay in your name."),
       ("Will you change my budget without asking?", "No. We recommend changes with the reason behind them, and you approve them."),
       ("Can ads send people to WhatsApp?", "Yes. Most of our local campaigns use WhatsApp as the destination, because that's where people in Kerala prefer to ask questions.")],
      "Hello Ad Pro, I'm interested in Meta & Google Ads.")

inner("posters-video-ads.html", "Posters & Video Ads", "Posters and reels in your customer's language.",
      "Posters, social creatives and short motion-graphics reels, in Malayalam and English, sized for every placement.",
      [("Posters and social creatives", "<p>Offer posters, course or product creatives, festival greetings and Google Business Profile images. Each design comes in every size the platforms need: square, story/reel and landscape.</p><p>Where you have brand guidelines, we follow them exactly: logo spacing, colours, the right phone number and website on every piece.</p>"),
       ("Motion-graphics video ads", "<p>15-second vertical reels built for Instagram and Facebook: bold animated text, your offer, and a clear call to action. We usually make two versions, one with the current offer and one evergreen, so the ad keeps running after the offer ends.</p>"),
       ("Malayalam and English", "<p>On-screen text in Malayalam and English, with an optional Malayalam voice-over. Your audience hears the offer in their own language even with captions off.</p>"),
       ("Corporate artwork, localised", "<p>Franchise and dealer businesses often get head-office creatives carrying the corporate phone number. We swap in your branch name, number and website before anything goes live.</p>")],
      [("Which sizes do I get?", "Square (1:1), story/reel (9:16) and landscape where needed, so the same creative works in feed, stories and reels."),
       ("Can you use our existing brand guidelines?", "Yes. Send the guideline PDF and logo files; we follow the colours, fonts and logo rules in them."),
       ("Do you make Malayalam voice-overs?", "Yes. Short reels can carry a Malayalam voice-over as well as Malayalam on-screen text.")],
      "Hello Ad Pro, I'm interested in Posters & Video Ads.")

inner("app-development.html", "App Development", "Your app. On every screen.",
      "Android, iPhone, web and Windows apps, designed, built and launched by Ad Pro. Tell us your idea and we take care of the rest.",
      [("What we build", ul(["<b>Android and iPhone apps</b> for phones and tablets", "<b>Android TV apps</b> for lobby and shop displays", "<b>Windows desktop apps</b> for billing, stock and front-office work",
            "<b>Web apps and dashboards</b> that run in the browser, with nothing to install",
            "<b>WhatsApp Business automation</b>: Cloud API auto-replies that answer common questions from your own data and step aside when your staff reply by hand",
            "<b>Integrations</b> with what you already use: Google Sheets, email, attendance and biometric devices, ad platforms"])),
       ("Built from your real workflow", "<p>We start with how your staff work today: who enters what, where the data lives and what keeps going wrong. Then we build only what removes that work. A good business app is usually small, and it fits the way people already do things.</p>"),
       ("Complete delivery", "<p>Design, development, testing on your devices, installation and staff hand-over. Source code is kept in a private repository, and app builds are produced automatically from it.</p>"),
       ("Example: a lobby TV attendance app", '<p>For a computer training centre we built an Android TV and mobile app. Tutors mark attendance from their phone, the lobby TV shows each batch live, and between batches the TV runs the centre\'s ads and information. It is now a product other centres can buy: <a href="batchboard.html">BatchBoard</a>.</p>')],
      [("Do you build iPhone apps?", "Yes. We build for Android, iPhone, web and Windows, so your app works on whatever your staff and customers use."),
       ("Who owns the app?", "You do. Custom apps are built for your business and handed over to you."),
       ("Can the app read data we already keep in Google Sheets?", "Yes. Many of our builds read from and write to the sheets your team already fills in, so nobody has to learn a new system.")],
      "Hello Ad Pro, I'm interested in App Development.")

inner("batchboard.html", "BatchBoard", "Attendance, live on your centre TV.",
      "A lobby TV app for computer and coaching centres: live batch attendance on screen, your ads in between.",
      [("What the TV shows", ul(["<b>Live batch boards</b>: from 15 minutes before each batch starts until 5 minutes after, the TV shows who has checked in and who is on leave.",
            "<b>An opening brief</b> when the centre opens for the day.", "<b>Between batches</b>: calm music, your video ads and useful information for students and parents waiting in the lobby."])),
       ("How attendance gets there", "<p>Tutors mark attendance from the BatchBoard app on their phone, and it appears on the TV at once. Leave can be marked too, so the board shows students on leave separately from those who have not arrived yet.</p>"),
       ("Made for a public lobby", ul(["Shows first name and initial only, never full names or phone numbers", "Batch boards run Monday to Friday; weekends show your content loop",
            "Styled to your centre's logo and brand colours", "Runs on any Android TV or Google TV box plugged into the TV you already have"])),
       ("Price", "<p><b>&#8377;5,000, one time.</b> No monthly subscription. Includes set-up on your TV box, branding to your centre, and showing your staff how to use it.</p>")],
      [("Is there a monthly fee?", "No. BatchBoard is ₹5,000 one-time, with no subscription."),
       ("What hardware do I need?", "A TV in your lobby and an Android TV or Google TV box connected to it, plus Android phones for the tutors who mark attendance."),
       ("Does it show students' full names?", "No. The TV shows first name and initial only, because it is on display in a public lobby."),
       ("Can we try it first?", "Yes. Message us on WhatsApp to arrange a demo.")],
      "Hello Ad Pro, I'd like a BatchBoard demo for my centre.", side_title="Book a demo", side_text="See BatchBoard running, then decide.",
      price="&#8377;5,000 one-time, no subscription", title="BatchBoard: lobby TV attendance app | Ad Pro Advertising")

# ---------------- WORK ----------------
work = f'''<section class="ph">{hands_svg("cs")}<div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Our work</div>
<h1 class="d1">Our work</h1><p class="lede">What we have built and run for each client. Every site below is live, so you can open it and judge it yourself.</p></div></section>
<section class="sec ink"><div class="wrap">{"".join(case_html(c, i, True) for i, c in enumerate(CASES))}</div></section>
{cta("Want results like these?", "Tell us what you sell and who buys it, and we'll show you what we'd build.")}'''
page("work.html", "Our work: websites, ads & apps | Ad Pro Advertising", "Live websites, ad campaigns and apps Ad Pro Advertising has built for clients in Kerala and Bengaluru.", work, crumbs_ld("Our work", "work.html"))

# ---------------- ABOUT ----------------
about = f'''<section class="ph">{hands_svg("cs")}<div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / About</div>
<h1 class="d1">We give local businesses a hand up.</h1><p class="lede">A digital marketing and development studio in Charummood, Alappuzha, working for businesses across Kerala and beyond.</p></div></section>
<section class="sec"><div class="wrap split">
<div><h2 class="d2">Two hands, one goal.</h2></div>
<div class="prose"><p>Our logo is two hands. The blue one on top is us, reaching down to help. The red one below is our client's business, reaching up for its next step. That's the job as we see it.</p>
<p>A small business doesn't need a pretty website. It needs more of the right people calling. So everything we make is judged on one question: does it bring in enquiries? That's why our websites are hand-coded for speed and local search, why our ads are checked against the leads that actually arrive, and why our creatives speak Malayalam when the customer does.</p></div>
</div></section>
<section class="sec mist"><div class="wrap">
<div class="sec-h"><h2 class="d2">How we work with clients</h2><p>Code, copywriting, poster design, motion video and app development are all done by our own team in Charummood. One team is responsible for the whole result.</p></div>
<div class="values"><div><h3>No changes without approval</h3><p>Budgets, campaigns and live pages change only after you say yes.</p></div>
<div><h3>You own your accounts</h3><p>Your domain, ad accounts and Google Business Profile stay in your name. We work as a partner on them.</p></div>
<div><h3>Plain reporting</h3><p>What was spent, what came in and what we suggest next, in a few lines.</p></div></div>
</div></section>
{cta()}'''
page("about.html", "About Ad Pro Advertising | Charummood, Alappuzha", "Ad Pro Advertising is a digital marketing and development studio in Charummood, Alappuzha, working for businesses across Kerala and beyond.", about, crumbs_ld("About", "about.html"))

# ---------------- CONTACT ----------------
opts = "".join(f"<option>{html.escape(s[1])}</option>" for s in SERVICES) + "<option>BatchBoard</option><option>Not sure yet</option>"
contact = f'''<section class="ph">{hands_svg("cs")}<div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Contact</div>
<h1 class="d1">Contact Ad Pro</h1><p class="lede">The quickest way to reach us is WhatsApp. Fill in the form and it opens WhatsApp with your message already written.</p></div></section>
<section class="sec"><div class="wrap"><div class="layout">
<form class="form" id="qf">
<div class="two"><label>Your name<input id="n" required autocomplete="name"></label><label>Business name<input id="b" autocomplete="organization"></label></div>
<div class="two"><label>Place<input id="p" placeholder="e.g. Charummood, Kayamkulam"></label><label>What do you need?<select id="s">{opts}</select></label></div>
<label>Tell us a little more<textarea id="m" rows="5" placeholder="What you sell, who your customers are, what you'd like to happen"></textarea></label>
<div><button class="btn btn-ink" type="submit">{WA_ICON} Send on WhatsApp</button></div>
<p class="note">Nothing is stored on this website. The form only writes your message into WhatsApp, and you press send there.</p>
</form>
<aside class="side"><div class="box dark"><h3>Call or WhatsApp</h3><p><a class="num" href="tel:{TEL}" style="color:#fff;font-size:1.7rem;text-decoration:none">{PHONE}</a></p>
<a class="btn btn-sky" href="{wa()}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a></div>
<div class="box"><h3>Find us</h3><p style="margin:0">Charummood, Alappuzha, Kerala</p><p class="small" style="margin:10px 0 0">Instagram <a class="link" href="https://www.instagram.com/adpro_advt/" target="_blank" rel="noopener">@adpro_advt</a></p></div></aside>
</div></div></section>'''
page("contact.html", "Contact Ad Pro Advertising | Call or WhatsApp 75609 21593", "Call or WhatsApp Ad Pro Advertising on 75609 21593, or send your project details through the contact form.", contact, crumbs_ld("Contact", "contact.html"))

# ---------------- 404 ----------------
nf = f'''<section class="ph" style="border:0">{hands_svg("cs")}<div class="wrap"><h1 class="d1">This page isn't here.</h1>
<p class="lede">The link may be old or mistyped. Try the home page, or message us and we'll point you to what you need.</p>
<div class="ctas"><a class="btn btn-ink" href="index.html">Go to the home page</a><a class="btn btn-line" href="{wa()}" target="_blank" rel="noopener">WhatsApp us</a></div></div></section>'''
page("404.html", "Page not found | Ad Pro Advertising", "This page could not be found.", nf)
s = open(os.path.join(OUT, "404.html")).read().replace('<head>', '<head>\n<meta name="robots" content="noindex">', 1)
open(os.path.join(OUT, "404.html"), "w").write(s)

# ---------------- static files ----------------
shutil.copy("site.css", f"{OUT}/site.css")
pages = ["index.html"] + [s[0] for s in SERVICES] + ["batchboard.html", "work.html", "about.html", "contact.html"]
sm = "".join(f"<url><loc>{SITE}/{'' if p=='index.html' else p}</loc><lastmod>2026-11-09</lastmod></url>" for p in pages)
open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(f"{OUT}/.htaccess", "w").write('''Options -Indexes
ErrorDocument 404 /404.html
DirectoryIndex index.html

<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [L,R=301]
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
RewriteCond %{THE_REQUEST} \\s/index\\.html[\\s?] [NC]
RewriteRule ^index\\.html$ / [L,R=301]
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 30 days"
ExpiresByType font/woff2 "access plus 1 year"
ExpiresByType image/svg+xml "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType image/jpeg "access plus 30 days"
ExpiresByType text/html "access plus 0 seconds"
</IfModule>
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/xml text/plain
</IfModule>
''')
print("built", len(pages) + 1, "pages")
