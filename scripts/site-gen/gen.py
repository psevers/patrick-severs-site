import hashlib, re, sys, pathlib
S = pathlib.Path(__file__).parent
OUT = pathlib.Path(__file__).resolve().parents[2]/"src"

# Active pages are rendered from templates. Legacy routes remain as explicit redirects
# so established links continue to work without presenting duplicated content.
ACTIVE_PAGES = {
  "index.html": ("Patrick Severs: GTM Leadership, Teams and AI Operations",
     "I turn strategy into revenue. Go-to-market leadership, team building, and AI operations, with the performance record to back it up.", "Home"),
  "gtm-leadership.html": ("Previous Performance: Patrick Severs",
     "Revenue growth, new business lines, and cross-functional leadership. The G2i record: 122% growth, four lines from one, and the team behind it.", "Previous performance"),
  "how-i-operate.html": ("How I Operate: Patrick Severs",
     "How I lead people, put agents to work, and keep responsibility clear. Six operating rules, the agent fleet, and the work built under my direction.", "How I operate"),
  "career.html": ("Career Overview: Patrick Severs",
     "From enterprise sales to leading revenue teams and new business lines. Patrick Severs at Dell, ServiceSource, ADP, Box, Braintrust, G2i, and The Agent Company.", "Career"),
}

NAV_ITEMS = [
  ("gtm-leadership.html", "Previous work"),
  ("how-i-operate.html", "How I operate"),
  ("career.html", "Career"),
]

LEGACY_REDIRECTS = [
  ("human-data-operating-layer.html", "/gtm-leadership.html#human-data", "Human Data"),
  ("agent-company.html", "/#now", "What I'm working on now"),
]

def head(fn, title, desc):
    url = "https://patricksevers.com/" + ("" if fn == "index.html" else fn)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://patricksevers.com/assets/images/og-image.png">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://patricksevers.com/assets/images/og-image.png">
<link rel="canonical" href="{url}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='18' fill='%23ffffff' stroke='%23101010' stroke-width='6'/%3E%3Ctext x='50' y='70' font-family='Arial,sans-serif' font-size='58' font-weight='700' fill='%23254e70' text-anchor='middle'%3EP%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="{'home' if fn == 'index.html' else 'sub'}">
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <marker id="wb-arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="var(--ink)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <marker id="wb-arrowhead-accent" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="var(--marker)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <filter id="wb-rough" x="-2%" y="-2%" width="104%" height="104%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="1.4" xChannelSelector="R" yChannelSelector="G"/></filter>
  </defs>
</svg>
'''

def nav(fn):
    CUR = ' aria-current="page"'
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (h, CUR if h == fn else "", l) for h, l in NAV_ITEMS
    )
    return f'''<nav class="nav">
  <div class="container">
    <a href="/" class="nav-logo">Patrick Severs <span>/ GTM</span></a>
    <ul class="nav-links" data-nav-links>
      {items}
      <li><a href="https://calendly.com/pvsevers/30min" class="nav-cta" target="_blank" rel="noopener">Book 30 minutes</a></li>
    </ul>
    <div class="nav-right">
      <button type="button" class="theme-toggle" data-theme-toggle>Dark mode</button>
      <button class="nav-toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
</nav>
'''

FOOTER = '''<footer class="footer" id="contact">
  <div class="container">
    <div class="footer-inner row">
      <div class="footer-text main">
        <h2>Let's talk.</h2>
        <p>Hiring a GTM leader, building a revenue team, or putting AI to work in the business? Let’s talk about what needs to change and how I can help.</p>
        <a href="mailto:pvsevers@gmail.com" class="mail">pvsevers@gmail.com</a>
      </div>
      <aside class="rail colophon m"><a href="assets/pdf/patrick-severs-resume.pdf" target="_blank" rel="noopener">Resume, one page</a><br><a href="https://calendly.com/pvsevers/30min" target="_blank" rel="noopener">Book 30 minutes</a><br><a href="https://www.linkedin.com/in/pvsevers/" target="_blank" rel="noopener">LinkedIn</a><br><a href="https://github.com/psevers" target="_blank" rel="noopener">GitHub</a></aside>
    </div>
    <div class="colophon-line fn">
      <span>Built around the work, the systems behind it, and the next revenue problem. Revised September 2026.</span>
      <button type="button" class="theme-toggle" data-theme-toggle>Dark mode</button>
    </div>
    <div class="footer-meta">
      <span>&copy; 2026 Patrick Severs</span>
      <span>Spring Hill, Tennessee</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
<script src="assets/js/loops.js"></script>
<script src="assets/js/riso.js" defer></script>
</body>
</html>
'''

LOOP_RE = re.compile(r'<!--loop:([a-z0-9-]+)(?::(\d+):(\d+))?-->')

def loop_media(m):
    stem, w, h = m.group(1), m.group(2) or "1280", m.group(3) or "714"
    jpg = f"assets/images/loops/{stem}.jpg"
    mp4 = OUT/"assets"/"video"/f"loop-{stem}.mp4"
    webm = OUT/"assets"/"video"/f"loop-{stem}.webm"
    img = f'<img src="{jpg}" alt="" width="{w}" height="{h}">'
    if not mp4.exists():
        return f'<div class="loop-media">{img}</div>'
    sources = ""
    if webm.exists():
        sources += f'<source src="assets/video/loop-{stem}.webm" type="video/webm">'
    sources += f'<source src="assets/video/loop-{stem}.mp4" type="video/mp4">'
    return (
        f'<div class="loop-media"><video autoplay muted loop playsinline preload="metadata" '
        f'disablepictureinpicture disableremoteplayback poster="{jpg}" width="{w}" height="{h}">'
        f'{sources}{img}</video></div>'
    )

def write_redirect(fn, dest, label):
    canonical = "https://patricksevers.com" + dest
    (OUT/fn).write_text(
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"UTF-8\">\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={dest}\">\n"
        f"<link rel=\"canonical\" href=\"{canonical}\">\n"
        f"<title>Moved: {label}</title>\n</head>\n"
        f"<body><p>This page moved to <a href=\"{dest}\">{label}</a>.</p></body>\n</html>\n"
    )
    print("wrote redirect", fn)

for fn, (title, desc, _) in ACTIVE_PAGES.items():
    body = LOOP_RE.sub(loop_media, (S/"pages"/fn).read_text())
    page = head(fn, title, desc) + nav(fn) + body + FOOTER
    for asset in ("assets/css/style.css", "assets/js/main.js", "assets/js/riso.js", "assets/js/loops.js"):
        version = hashlib.sha256((OUT/asset).read_bytes()).hexdigest()[:12]
        page = page.replace(f'"{asset}"', f'"{asset}?v={version}"')
    (OUT/fn).write_text(page)
    print("wrote", fn)

for fn, dest, label in LEGACY_REDIRECTS:
    write_redirect(fn, dest, label)
