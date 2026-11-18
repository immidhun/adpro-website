"""Blog posts for adproadvertising.in. build.py turns each one into /blog/<slug>.html.

House rules (Ad Pro brand guidelines): plain English, short sentences, lead with what the reader gets,
name real places and real work, no invented numbers, awards or reviews, no prices unless already approved,
end with one clear action. Every factual claim about Google or Meta must be backed by a listed source.
"""

G_RANK = ("Google Business Profile Help: how Google determines local ranking", "https://support.google.com/business/answer/7091?hl=en")
G_RULES = ("Google Business Profile: guidelines for representing your business", "https://support.google.com/business/answer/3038177?hl=en")
G_REVIEWS = ("Google Maps: prohibited and restricted content", "https://support.google.com/contributionpolicy/answer/7400114?hl=en")
G_MOVE = ("Google Search Central: site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes")
G_LOCAL_SD = ("Google Search Central: local business structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business")
M_CTWA = ("Meta for Developers: ads that click to WhatsApp", "https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp/")
W_CTWA = ("WhatsApp Business: best practices for ads that click to WhatsApp", "https://business.whatsapp.com/resources/resource-library/whatsapp-business-app-resources/ads-that-click-to-whatsapp-best-practices")

POSTS = [
    dict(
        slug="google-maps-listing-alappuzha-business",
        date="2026-11-18",
        cat="Local SEO",
        service="website-design-local-seo.html",
        service_name="Websites & Local SEO",
        cover="Get your business on Google Maps.",
        seo="How to Get Your Alappuzha Business on Google Maps | Ad Pro",
        title="How to get your Alappuzha business on Google Maps",
        desc="A plain-English guide to setting up a Google Business Profile in Alappuzha: name, address, category, hours, photos, reviews and the mistakes to avoid.",
        lede="When someone nearby searches for what you sell, the map is often the first thing they see. Here is how to get your business onto it, and how to keep it there.",
        keys=["Your listing is a free Google Business Profile.",
              "Google ranks local results on relevance, distance and prominence. You cannot pay for a better local position.",
              "Use your real business name. Adding keywords to it breaks Google's rules.",
              "Ask real customers for reviews, but never offer anything in return."],
        body="""
<h2>Start with a Google Business Profile</h2>
<p>Your place on Google Maps comes from a Google Business Profile. It is free, and it is the same listing that shows your phone number, hours, photos and reviews in Google Search.</p>
<p>Before you create one, search for your business on Google Maps. A listing may already exist, added by a customer or a previous owner. If it does, claim it instead of making a second one. Google allows only one profile per location.</p>

<h2>Set it up in five steps</h2>
<ol>
<li><b>Sign in</b> at <a href="https://business.google.com" rel="noopener" target="_blank">business.google.com</a> with a Google account your business will keep. Avoid a staff member's personal account.</li>
<li><b>Enter your business name</b> exactly as it appears on your board and bills.</li>
<li><b>Choose your category.</b> Pick the most specific one that finishes the sentence "this business is a...".</li>
<li><b>Add your address or service area.</b> If customers come to you, show the address. If you travel to them, set a service area and hide the address.</li>
<li><b>Verify the business.</b> Google will show you the verification method available for your listing. Your profile is not fully trusted until this is done.</li>
</ol>

<h2>The rules that catch people out</h2>
<p>Most listing problems come from trying to look bigger or rank faster. Google's guidelines are clear on these:</p>
<ul>
<li><b>No extra words in the name.</b> "Sree Bakery" is fine. "Sree Bakery Best Cakes Alappuzha" is not, unless that is truly your registered, signboard name.</li>
<li><b>No virtual offices or PO boxes.</b> The address must be a real place you operate from.</li>
<li><b>One phone number you control.</b> Do not use a number that forwards callers somewhere else.</li>
<li><b>Link to your own website.</b> Google does not accept redirecting links or social media pages in the website field.</li>
<li><b>Few, accurate categories.</b> Categories describe what your business is, not everything you sell.</li>
</ul>

<h2>What decides who shows first</h2>
<p>Google says local results depend mainly on three things:</p>
<ul>
<li><b>Relevance:</b> how well your profile matches the search.</li>
<li><b>Distance:</b> how far you are from the person searching, or from the place named in the search.</li>
<li><b>Prominence:</b> how well known you are, including links from other websites and the number and rating of your reviews.</li>
</ul>
<p>You cannot change where a customer is standing. You can make your profile complete and earn more genuine reviews. Google also states that there is no way to pay for a better local ranking, so be careful of anyone selling a guaranteed top spot.</p>

<h2>Keep the listing alive</h2>
<ul>
<li>Update your hours before Onam, Vishu, Christmas and other holidays, using special hours.</li>
<li>Add real photos of your shop, team and work. Skip stock images.</li>
<li>Reply to every review, including the unhappy ones. Keep it short and polite.</li>
<li>Check that your name, address and phone match your website exactly.</li>
</ul>

<h2>Getting reviews the right way</h2>
<p>Ask happy customers at the moment they are happiest: when the job is finished or the order is delivered. Send them your review link on WhatsApp so it takes one tap.</p>
<p>Do not offer discounts, gifts or payment for a review. Google removes incentivised reviews from Maps, and staff or family reviews can count as a conflict of interest.</p>
""",
        sources=[G_RANK, G_RULES, G_REVIEWS],
        action="Want your listing set up or cleaned up? Google Business Profile set-up comes with every website we build.",
    ),
    dict(
        slug="local-seo-checklist-kerala-small-business",
        date="2026-11-18",
        cat="Local SEO",
        service="website-design-local-seo.html",
        service_name="Websites & Local SEO",
        cover="The local SEO checklist.",
        seo="Local SEO Checklist for Kerala Small Businesses | Ad Pro",
        title="Local SEO checklist for small businesses in Kerala",
        desc="A practical local SEO checklist for Kerala businesses: Google profile, service and area pages, page titles, structured data, speed, reviews and tracking.",
        lede="Local SEO means showing up when people near you search for what you sell. Work through this list in order. The first items usually matter most.",
        keys=["Fix your Google Business Profile before anything else.",
              "Give each main service its own page.",
              "Only build area pages you can make genuinely useful.",
              "Measure enquiries, not just rankings."],
        body="""
<h2>1. Get the basics of your listing right</h2>
<ul>
<li>Your Google Business Profile is claimed and verified.</li>
<li>Name, category, hours and service area are accurate.</li>
<li>Real photos are added and reviews get replies.</li>
</ul>
<p>Our guide to <a href="google-maps-listing-alappuzha-business.html">getting on Google Maps</a> covers each of these step by step.</p>

<h2>2. Keep your name, address and phone identical</h2>
<p>Write your business details once, then copy them everywhere: website, Google profile, Facebook, Instagram and business directories. If one site says "Road" and another says "Rd", that is minor. A different phone number or an old address is the kind of mismatch to fix first, because it sends customers to the wrong place.</p>

<h2>3. Build one page for each service</h2>
<p>A single "Services" page with a list of ten items gives Google very little to match. A page for each main service can answer the real questions: what is included, who it suits, how it works and how to contact you.</p>
<p>Think about the words customers actually type. A family looking for help at home may search "home nurse near me", not your company name. Write the page for that person.</p>

<h2>4. Add area pages only if they say something real</h2>
<p>If you serve several towns, a page for each can help. But copying one page and swapping "Kayamkulam" for "Mavelikkara" helps nobody. A useful area page says something specific: delivery days, the local branch, nearby landmarks or the work you have done there.</p>
<p>For <a href="../work.html#sg">S&amp;G Polymers</a>, a bottle manufacturer in Punnapara, we built a Kerala delivery page plus six district pages, so buyers can find a page written for their area.</p>

<h2>5. Get the on-page details right</h2>
<ul>
<li><b>Page title:</b> say what the page offers and where. Keep it short enough to read in search results.</li>
<li><b>Meta description:</b> one or two sentences that make someone want to click.</li>
<li><b>One clear main heading</b> on each page, with sub-headings that follow the content.</li>
<li><b>Image descriptions</b> that say what the picture actually shows.</li>
<li><b>Links between pages,</b> so people and Google can find related services.</li>
</ul>

<h2>6. Add structured data</h2>
<p>Structured data is a small block of code that tells search engines your business name, address, phone and more in a format they can read reliably. For local businesses, Google requires a name and address and recommends details such as phone number, website, opening hours and map coordinates. Only mark up information that is true and visible to customers.</p>

<h2>7. Make it fast on a phone</h2>
<p>Most of your visitors will arrive on mobile data. Compress images, remove plugins you do not need and test your pages on an ordinary phone. Your phone number and WhatsApp button should be easy to reach without hunting.</p>

<h2>8. Earn reviews and local mentions</h2>
<p>Ask real customers for reviews. Get listed in trusted local directories, your trade association and the websites of partners you actually work with. Google counts links and reviews among the signals of how well known a business is.</p>

<h2>9. Measure what matters</h2>
<p>Connect Google Search Console and Google Analytics 4. Then keep a simple record of calls and WhatsApp enquiries, and ask each new customer how they found you. A rising ranking means little if the phone stays quiet.</p>
""",
        sources=[G_RANK, G_RULES, G_LOCAL_SD],
        action="Rather have it done for you? This whole list is part of every website we deliver.",
    ),
    dict(
        slug="rebuild-website-without-losing-google-rankings",
        date="2026-11-18",
        cat="Websites",
        service="website-design-local-seo.html",
        service_name="Websites & Local SEO",
        cover="New website. Keep your Google rankings.",
        seo="Rebuild Your Website Without Losing Rankings | Ad Pro",
        title="How to rebuild your website without losing Google rankings",
        desc="Planning a new website? Follow these steps to protect your Google rankings: list every old URL, keep what works, use 301 redirects and check the launch.",
        lede="A new website can quietly wipe out years of search visibility if old pages simply disappear. The fix is careful planning before anything goes live.",
        keys=["List every existing page before you change anything.",
              "Keep the same address wherever you can.",
              "Send each old address to its closest new page with a 301 redirect.",
              "Keep redirects for at least a year, and expect some short-term movement."],
        body="""
<h2>Why rebuilds lose traffic</h2>
<p>Google knows your site as a set of addresses. If <i>/courses/tally.html</i> ranks today and vanishes tomorrow, searchers land on an error page and Google has no clear replacement to show. The new design may look better, but the page that earned the ranking is gone.</p>

<h2>Step 1: List everything you have now</h2>
<p>Before any design work, collect every address on the current site. Use your sitemap, Google Search Console, analytics and a crawl of the site. Include images and PDFs that people may link to.</p>
<p>Mark the pages that matter most: those that bring in visitors, have links from other websites or lead to enquiries.</p>

<h2>Step 2: Keep addresses where you can</h2>
<p>The safest redirect is the one you never need. If a page keeps its purpose, try to keep its exact address on the new site, even if the design changes completely.</p>
<p>When we rebuilt the <a href="../work.html#gtec">G-TEC Computer Education, Charummood</a> website, all 28 existing pages were carried across. 21 kept their exact address, and the rest were permanently redirected.</p>

<h2>Step 3: Map the old to the new</h2>
<p>Make a simple spreadsheet with two columns: old address and new address. Every old page gets a row. Then check three things:</p>
<ul>
<li>Each old page points to the closest matching new page.</li>
<li>Redirects go straight to the final page, with no chains.</li>
<li>You are not sending many old pages to the home page. Google specifically advises against redirecting lots of old addresses to an unrelated page.</li>
</ul>

<h2>Step 4: Use permanent redirects</h2>
<p>Set up server-side 301 redirects. They tell browsers and Google that the page has moved for good. Google recommends keeping them in place for at least one year, so do not delete them after launch.</p>

<h2>Step 5: Carry the content across</h2>
<p>A redirect cannot save a page whose useful content was removed. Keep the details that made it rank: service information, answers to common questions, fees where you publish them, and location details. Copy across page titles and descriptions too, then improve them with care.</p>

<h2>Step 6: Check launch day</h2>
<ol>
<li>Test the old addresses from your spreadsheet. Each should land on the right new page.</li>
<li>Make sure the new site is not blocked from search engines. A leftover "noindex" tag from the test site is a common mistake.</li>
<li>Submit the new sitemap in Search Console.</li>
<li>Confirm your phone links, WhatsApp buttons and forms all work.</li>
<li>Update the website link on your Google Business Profile if the address changed.</li>
</ol>
<p>If you are also moving to a new domain, use the Change of Address tool in Search Console.</p>

<h2>What to expect afterwards</h2>
<p>Even a well-run move can cause some ranking changes while Google recrawls the site. Google says this can take a few weeks or more for a medium-sized site. So avoid launching just before your busiest season, and watch Search Console for pages reporting errors.</p>
""",
        sources=[G_MOVE],
        action="Planning a rebuild? We list your existing pages first, so the rankings you have earned are protected.",
    ),
    dict(
        slug="whatsapp-ads-real-enquiries",
        date="2026-11-18",
        cat="Ads",
        service="meta-google-ads.html",
        service_name="Meta & Google Ads",
        cover="WhatsApp ads: find the real enquiries.",
        seo="WhatsApp Ads: How to Spot Real Enquiries | Ad Pro",
        title="WhatsApp ads: how to tell which enquiries are real",
        desc="Click-to-WhatsApp ads can fill your inbox without filling your order book. Learn how local businesses can track which ads bring real customers.",
        lede="A cheap conversation looks great in Ads Manager. But a chat is not a customer. Here is a simple way to see which WhatsApp ads actually bring in business.",
        keys=["A \"conversation started\" only tells you someone opened a chat.",
              "A simple enquiry sheet shows what happened next.",
              "Give each ad its own opening message so you can tell them apart.",
              "On small budgets, wait for a pattern before changing things."],
        body="""
<h2>What the ad platform can and cannot see</h2>
<p>Click-to-WhatsApp ads open a chat with your business when someone taps the ad on Facebook or Instagram. That makes them a natural fit for local businesses, because customers can ask a question in the app they already use.</p>
<p>Meta can report how many people clicked and started a conversation. Unless your WhatsApp system sends results back to Meta, it does not know what happened inside that chat. It cannot tell whether the person was serious, visited your shop or paid you. Your team knows that.</p>

<h2>Keep a simple enquiry sheet</h2>
<p>You do not need expensive software to start. A shared Google Sheet is enough. Add one row for each enquiry:</p>
<ul>
<li>Date</li>
<li>Name and phone number</li>
<li>Which ad or offer they came from</li>
<li>What they asked for</li>
<li>Status: replied, interested, visited, bought or not interested</li>
<li>Reason, if the enquiry was lost</li>
</ul>
<p>Keep the sheet private, because it holds customer details. Limit access to the staff who need it.</p>

<h2>Make every ad identifiable</h2>
<p>You can set the first message that appears in the customer's chat. Use a different one for each campaign. For example:</p>
<ul>
<li>"Hi, I'd like details of the Onam offer."</li>
<li>"Hi, I'd like to know about the weekend batch."</li>
</ul>
<p>When the message arrives, staff can tell which ad brought that person in and record it. It is a small step, and it makes the sheet far more reliable.</p>

<h2>Reply fast, and the same way every time</h2>
<p>A paid enquiry can go cold while it waits. Decide who answers, during which hours and what happens after closing time. Use saved replies for common questions, but let a person take over as soon as the conversation needs one.</p>
<p>Make sure every reply matches your website and posters. If an ad offers one thing and staff quote another, you lose trust and the sale.</p>

<h2>Compare ads on what they actually produce</h2>
<p>At the end of each week, line up your ad spend against the sheet. Work out three figures for each campaign:</p>
<ol>
<li><b>Cost per conversation:</b> what the platform shows you.</li>
<li><b>Cost per interested enquiry:</b> spend divided by people who were genuinely interested.</li>
<li><b>Cost per customer:</b> spend divided by people who bought.</li>
</ol>
<p>The ad with the cheapest conversations is not always the winner. One that brings fewer chats but more buyers is usually the better ad.</p>

<h2>Do not overreact to one week</h2>
<p>With only a few enquiries a week, one good or bad week means very little. Wait until you see a consistent pattern before you cut an audience or move your budget. And turn off offer ads the day the offer ends, so people are not messaging about a deal that has gone.</p>
""",
        sources=[M_CTWA, W_CTWA],
        action="Want ads judged on real enquiries? We check campaigns against your enquiry sheet, and no budget changes without your approval.",
    ),
    dict(
        slug="malayalam-or-english-ads",
        date="2026-11-18",
        cat="Creatives",
        service="posters-video-ads.html",
        service_name="Posters & Video Ads",
        cover="Malayalam or English?",
        seo="Malayalam or English: Which Language for Your Ads? | Ad Pro",
        title="Malayalam or English: which language should your ad use?",
        desc="How Kerala businesses can choose between Malayalam and English for posters and reels, with practical tips on audience, readability, voice-over and testing.",
        lede="The right language depends on who you want to reach and what you are selling. Here is a practical way to decide, and how to make either choice work.",
        keys=["Start with the customer, not your own preference.",
              "Keep one message on each poster or reel.",
              "Make the offer clear with the sound off.",
              "Test both versions and judge them on enquiries."],
        body="""
<h2>Start with who is reading</h2>
<p>Picture the person who decides to buy. A parent choosing a course for their child, a family arranging care for an elderly relative and an IT manager ordering equipment may all read differently.</p>
<p>Ask your front-office staff what language customers use when they call or message. Look through your WhatsApp enquiries too. Your own customers are better evidence than any general rule.</p>

<h2>When Malayalam usually makes sense</h2>
<ul>
<li>Your customers are mostly local households.</li>
<li>The message is emotional or depends on trust, such as healthcare, family services or education for children.</li>
<li>You are explaining an offer that must be understood instantly.</li>
<li>You want a voice-over that sounds like someone from the area.</li>
</ul>

<h2>When English may work better</h2>
<ul>
<li>You sell to other businesses or to professionals.</li>
<li>Your audience reaches beyond Kerala.</li>
<li>Customers normally search for the product by its English name, as with many software courses and technical services.</li>
</ul>

<h2>Mixing both, without the clutter</h2>
<p>Many good Kerala ads use both languages, with each doing one job. A Malayalam headline can carry the message, while English handles the terms people already use, such as "Tally", "Python" or "WhatsApp". Keep your phone number and brand name easy to spot.</p>
<p>Avoid saying everything twice on one poster. That halves the space and makes both versions harder to read. If you need full versions in each language, make two creatives.</p>

<h2>Get the Malayalam right</h2>
<ul>
<li><b>Write it, do not machine-translate it.</b> Literal translations can sound stiff or simply wrong.</li>
<li><b>Use a font made for Malayalam,</b> and check that every conjunct letter displays correctly.</li>
<li><b>Allow more room.</b> Malayalam text can need more height and space than the English layout allowed for.</li>
<li><b>Have a native reader check the final artwork,</b> not just the typed copy.</li>
</ul>

<h2>Plan reels for silent viewing</h2>
<p>Many people scroll with the sound off, so your on-screen text must tell the story alone. A voice-over then adds warmth for those listening. In a short reel, keep it simple:</p>
<ol>
<li>Show what the customer gets in the first moments.</li>
<li>Give one reason to believe it.</li>
<li>End with one action and your phone number on screen.</li>
</ol>
<p>Use licensed or royalty-free music only. Film songs can get your ad blocked and create copyright trouble.</p>

<h2>Test it instead of guessing</h2>
<p>Run a Malayalam and an English version with the same offer, audience and budget. Give each its own WhatsApp opening message, so you can <a href="whatsapp-ads-real-enquiries.html">see which one brings real enquiries</a>. Judge the result on genuine interest, not likes.</p>
""",
        sources=[],
        action="Need posters or reels in Malayalam and English? We write, design and animate them in-house.",
    ),
    dict(
        slug="training-centre-live-attendance-tv",
        date="2026-11-18",
        cat="Apps",
        service="batchboard.html",
        service_name="BatchBoard",
        cover="Live attendance on your lobby TV.",
        seo="Live Attendance on a Training Centre TV | Ad Pro",
        title="How to show live attendance on your training centre's TV",
        desc="Turn your training centre's lobby TV into a live attendance board. What to show, how to protect student privacy and how to use the screen between batches.",
        lede="The TV in your lobby can do more than play the news. It can show who has arrived for each batch, then promote your courses while the room is quiet.",
        keys=["Tutors mark attendance on a phone and the TV updates.",
              "Show only what is needed. A lobby is a public place.",
              "Separate \"on leave\" from \"not arrived yet\".",
              "Between batches, use the screen for your own ads and notices."],
        body="""
<h2>Why put attendance on a screen?</h2>
<p>At the start of each batch, front-office staff often face the same questions. Has this student come? Is the tutor marking attendance? Who is on leave? A live board in the lobby makes the answer visible to everyone, without anyone leaving the desk.</p>
<p>It also shows parents and visitors that the centre is organised. That matters when someone is sitting in your lobby deciding whether to join.</p>

<h2>What a good board shows</h2>
<ul>
<li>The batch name and start time</li>
<li>Students who have checked in</li>
<li>Students on leave, shown separately</li>
<li>Students still expected</li>
</ul>
<p>The board should be readable from across the room. Use large text, a few clear colours and no scrolling tables.</p>

<h2>Protect student privacy</h2>
<p>A lobby is public. Anyone walking in can read the screen, so show as little as possible. Use first name and initial only. Never show full names, phone numbers, fee details or marks. Tell students and parents what the screen displays.</p>

<h2>Make marking attendance easy for tutors</h2>
<p>A system only works if tutors keep using it. Marking should take moments on the phone already in their hand, with no register to carry to the office and no second entry later. Leave should be just as quick, so the board stays accurate.</p>

<h2>Time the board around your batches</h2>
<p>The attendance board does not need to run all day. It is most useful just before and just after a batch begins. BatchBoard, for example, shows each board from 15 minutes before the batch starts until 5 minutes after.</p>

<h2>Use the quiet time for marketing</h2>
<p>Between batches, the same screen can run your own content for the people waiting:</p>
<ul>
<li>New courses and upcoming batch dates</li>
<li>Offers and admission deadlines</li>
<li>Student achievements, shared with permission</li>
<li>Centre notices and holiday timings</li>
</ul>
<p>Keep each message short and keep your phone number on screen. Remove old offers on time.</p>

<h2>What you need</h2>
<ol>
<li>A TV in the lobby</li>
<li>An Android TV or Google TV box connected to it</li>
<li>Android phones for the tutors who mark attendance</li>
<li>A stable internet connection</li>
</ol>

<h2>The app we built for this</h2>
<p>We first built this for a computer training centre in Charummood. It is now <a href="../batchboard.html">BatchBoard</a>, a lobby TV app for training and coaching centres. It is styled to your centre's logo and colours, and costs &#8377;5,000 one-time, with no subscription.</p>
""",
        sources=[],
        action="Want to see it running? Message us and we will arrange a BatchBoard demo for your centre.",
    ),
]


# Further sections, added after each post's main body.
EXTRA = {
    "google-maps-listing-alappuzha-business": """
<h2>Common questions</h2>
<h3>Can I list a business I run from home?</h3>
<p>Yes, if you meet customers in person. If they do not visit your home, set a service area and hide the address. Your listing can then show the places you cover without publishing where you live.</p>
<h3>Do I need a website to have a listing?</h3>
<p>No, but a website gives Google and your customers much more to go on. It can explain each service, show your work and answer questions a short listing cannot.</p>
<h3>What if someone else controls my listing?</h3>
<p>Start by finding out who has access. It may be a former employee, a relative or an agency. Ask them to add you as an owner. If you cannot reach them, use the access request option Google offers on the listing.</p>
<h3>What should I do about a bad review?</h3>
<p>Reply calmly, stick to the facts and offer to sort the problem out. Report a review only if it breaks Google's rules, for example if it is fake or was not based on a real experience. Never offer a customer anything to change or remove a review.</p>
<h3>We moved. What needs changing?</h3>
<p>Update the address on your profile first, then on your website, social pages and directory listings. Change your signboard and printed material too, so everything tells customers the same thing.</p>
<h2>A quick monthly routine</h2>
<ol>
<li>Search for your business the way a customer would, and check every detail.</li>
<li>Reply to any new reviews and questions.</li>
<li>Add a few recent photos of real work.</li>
<li>Check upcoming holidays and set special hours.</li>
<li>Ask your recent happy customers for a review.</li>
</ol>
""",
    "local-seo-checklist-kerala-small-business": """
<h2>A sensible order to work in</h2>
<p>You do not have to finish everything at once. If time is short, work in this order:</p>
<ol>
<li><b>First:</b> claim your Google profile and correct your name, address, phone and hours.</li>
<li><b>Next:</b> make sure your website works well on a phone, and that calling or messaging you is easy.</li>
<li><b>Then:</b> improve your main service pages, one at a time, starting with what earns you the most.</li>
<li><b>After that:</b> add structured data, connect your tracking and start asking for reviews.</li>
<li><b>Keep going:</b> add useful area pages and guides based on what customers ask you.</li>
</ol>
<h2>Mistakes that waste your effort</h2>
<ul>
<li><b>Stuffing place names into every sentence.</b> Write for the person reading.</li>
<li><b>Copying the same page for every town.</b> Those pages add little and are hard to keep accurate.</li>
<li><b>Buying reviews.</b> Paid and incentivised reviews break Google's rules and can be removed.</li>
<li><b>Using a different phone number on each platform.</b> Customers should reach the same business everywhere.</li>
<li><b>Hiding your services inside images.</b> Important details should be real text on the page.</li>
<li><b>Trusting guaranteed rankings.</b> Nobody can promise a position, and Google says local ranking cannot be bought.</li>
</ul>
<h2>Common questions</h2>
<h3>How long does local SEO take?</h3>
<p>There is no honest fixed answer. It depends on your competition, the state of your current website and profile, and how consistently the work is done. Corrections to your listing can help customers straight away, while content and reputation build over time.</p>
<h3>Should my website be in Malayalam too?</h3>
<p>If your customers search or prefer to read in Malayalam, it can be worth having properly written Malayalam pages. Check your enquiries first, and avoid publishing rough machine translation.</p>
<h3>Can I do this myself?</h3>
<p>Much of it, yes. The listing, reviews and page writing are well within reach of a business owner. Structured data, redirects and speed work are where technical help usually pays off.</p>
""",
    "rebuild-website-without-losing-google-rankings": """
<h2>Mistakes to avoid</h2>
<ul>
<li><b>Deleting old pages because they look outdated.</b> Update them or redirect them to a true replacement.</li>
<li><b>Changing the design, addresses, content and domain all at once</b> without a plan. The more that changes, the harder any drop is to trace.</li>
<li><b>Leaving the test site open to Google.</b> Protect it so unfinished pages do not appear in search.</li>
<li><b>Forgetting images and PDFs.</b> Brochures and price lists may have their own links and visitors.</li>
<li><b>Removing redirects when you change hosting.</b> Add them to your launch checklist for every future move.</li>
</ul>
<h2>Common questions</h2>
<h3>What if an old page has no equivalent on the new site?</h3>
<p>First ask whether it should have one. If people still need that information, keep or rewrite it. If the service has truly ended and nothing similar exists, let the address return a proper "not found" response. Do not send it to the home page just to avoid an error.</p>
<h3>Is changing only my hosting risky?</h3>
<p>It is usually simpler, because the addresses and content stay the same. Still copy everything carefully, check that redirects and security settings came across, and test the site before and after pointing the domain to the new server.</p>
<h3>Can I change my domain name at the same time?</h3>
<p>You can, but plan it with extra care. Redirect each old page to its match on the new domain, verify both domains in Search Console and use the Change of Address tool. Update your Google profile, social pages and printed material as well.</p>
<h3>What should I check in the weeks after launch?</h3>
<p>Watch the page indexing and performance reports in Search Console. Look for important pages that have dropped out, unexpected "not found" errors and redirects that fail. Above all, compare your calls and WhatsApp enquiries with the period before launch.</p>
""",
    "whatsapp-ads-real-enquiries": """
<h2>Ask better first questions</h2>
<p>Your first reply can do two jobs: help the customer and show how serious the enquiry is. Keep it friendly, and ask only what you need to give a useful answer:</p>
<ul>
<li>Which product, course or service are you looking for?</li>
<li>Where are you located?</li>
<li>When do you need it?</li>
<li>Is this for you or for someone else?</li>
</ul>
<p>Avoid sending a long form as your first message. Answer their question first, then ask one thing at a time.</p>
<h2>Should the ad go to WhatsApp or your website?</h2>
<p>Use WhatsApp when people usually want to ask a question before deciding, and you have staff ready to reply. Use a website page when the buyer needs detail, such as a full course outline or product range, or when you want them to read before they contact you.</p>
<p>Many local businesses use both. The important thing is to record where each enquiry came from, so you can compare them fairly.</p>
<h2>Follow up without becoming a nuisance</h2>
<p>Agree a simple rule with your team: for example, one helpful follow-up after an unanswered quote, then leave it. Note the outcome in your sheet. Only send offers to people who have agreed to hear from you, and stop when someone asks you to.</p>
<h2>Common questions</h2>
<h3>Why am I getting many chats but few customers?</h3>
<p>Look at the whole path. The ad may be too broad or the offer unclear. The audience may be outside your area. Replies may be slow, or the price and details may only become clear late in the chat. Your enquiry sheet will show where people drop away.</p>
<h3>Do I need the WhatsApp Business API?</h3>
<p>Not to start. The WhatsApp Business app can be enough for a small team. Consider the API when you need automation, several staff handling chats or results sent back to your ad account.</p>
""",
    "malayalam-or-english-ads": """
<h2>Examples by type of business</h2>
<ul>
<li><b>Training centre:</b> a Malayalam headline can speak to parents and students, while course names such as "Tally" stay in English.</li>
<li><b>Home-care service:</b> Malayalam can feel reassuring for families in Kerala. If you also serve relatives abroad or customers in another city, make a separate version for them.</li>
<li><b>Manufacturer or wholesaler:</b> English product names and sizes may be clearer for buyers, with Malayalam used for a local offer.</li>
<li><b>Shop or restaurant:</b> short, warm Malayalam can work well for neighbourhood offers and festival greetings.</li>
</ul>
<p>Treat these as starting points. Your own customers and results should have the final say.</p>
<h2>A quick check before you publish</h2>
<ol>
<li>Can someone understand the offer in a few seconds?</li>
<li>Does the design carry one main message?</li>
<li>Is the text large enough on a phone?</li>
<li>Has a fluent reader checked the spelling?</li>
<li>Are the phone number, place and dates correct?</li>
<li>Do the poster, reel and website all say the same thing?</li>
<li>Do you have the right to use the music and images?</li>
</ol>
<h2>Common questions</h2>
<h3>Should we use Malayalam written in English letters?</h3>
<p>It can feel casual and familiar in chats and some social posts. It is usually harder to read in longer lines, so use it sparingly and test it. For a formal message, proper Malayalam script or clear English is often the safer choice.</p>
<h3>Do we need a separate reel for each language?</h3>
<p>If each language needs its own voice-over and full text, yes. For a simple offer, one reel can use a Malayalam headline with familiar English product names.</p>
<h3>Which sizes should we make?</h3>
<p>Plan for square feed posts and vertical stories or reels at minimum. Keep important text away from the edges, where app buttons can cover it.</p>
""",
    "training-centre-live-attendance-tv": """
<h2>How to roll it out smoothly</h2>
<ol>
<li><b>Start with one batch.</b> Let one tutor use it for a few days and note what is confusing.</li>
<li><b>Agree the rules.</b> Decide who marks attendance, by when, and who records leave.</li>
<li><b>Tell students and parents.</b> Explain what appears on screen and why.</li>
<li><b>Place the TV carefully.</b> It should be easy to read from the waiting area and away from strong glare.</li>
<li><b>Prepare your content.</b> Have your course ads and notices ready before the first day.</li>
<li><b>Review after the first week,</b> then add the remaining batches.</li>
</ol>
<h2>Questions to ask before choosing a system</h2>
<ul>
<li>Does it work on the TV you already have, or with a low-cost box?</li>
<li>Can tutors mark attendance without training that takes days?</li>
<li>What exactly appears on the public screen?</li>
<li>Can you control your own ads and notices?</li>
<li>Is there a monthly fee, or a one-time cost?</li>
<li>Who helps if something stops working?</li>
<li>What happens if the internet connection drops?</li>
</ul>
<h2>Common questions</h2>
<h3>Does this replace our attendance records?</h3>
<p>That depends on the system and your centre's requirements. If you must keep formal registers for a course or an authority, confirm what is accepted before you change anything.</p>
<h3>What should the TV show at weekends?</h3>
<p>If you have no regular batches, run your content loop. BatchBoard shows batch boards from Monday to Friday and your content at weekends.</p>
<h3>Will parents be comfortable with this?</h3>
<p>They are more likely to be if you keep the display minimal and explain it clearly. First name and initial are enough for a lobby, and anything more personal should stay off the screen.</p>
""",
}
for _p in POSTS:
    _p["body"] += EXTRA[_p["slug"]]
