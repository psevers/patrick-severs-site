import re, sys, pathlib
S = pathlib.Path(__file__).parent
OUT = pathlib.Path(__file__).resolve().parents[2]/"src"

PAGES = {
  "index.html": ("Patrick Severs: GTM Leadership, Teams and AI Operations",
     "I turn strategy into revenue. Go-to-market leadership, team building, and AI operations, with the performance record and working notes to back it up.", "Home"),
  "gtm-leadership.html": ("Previous Performance: Patrick Severs",
     "Revenue growth, new business lines, and cross-functional leadership. The G2i record, plus earlier work in enterprise sales, renewals, and account expansion.", "Previous performance"),
  "human-data-operating-layer.html": ("Human Data: Patrick Severs",
     "A working blueprint for building a human-data business: the team, go-to-market motion, delivery, quality, and economics, with whiteboard diagrams.", "Human Data"),
  "agent-company.html": ("What I'm Working On Now: Patrick Severs",
     "Building go-to-market at The Agent Company. Working notes from day 45: the product decision, the operating work, and the first paid pilots.", "Now"),
  "how-i-operate.html": ("How I Operate: Patrick Severs",
     "How I lead people, put agents to work, and keep responsibility clear. Six operating rules, the agent fleet, and the work built under my direction.", "How I operate"),
  "career.html": ("Career Overview: Patrick Severs",
     "From enterprise sales to leading revenue teams and new business lines. Patrick Severs at Dell, ServiceSource, ADP, Box, Braintrust, G2i, and The Agent Company.", "Career"),
}

NAV_ITEMS = [
  ("gtm-leadership.html", "Previous work"),
  ("how-i-operate.html", "How I operate"),
  ("human-data-operating-layer.html", "Human Data"),
  ("agent-company.html", "Now"),
  ("career.html", "Career"),
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
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='18' fill='%23f6f4ee' stroke='%231b1a17' stroke-width='6'/%3E%3Ctext x='50' y='70' font-family='Georgia,serif' font-size='58' font-weight='600' fill='%231f4fd1' text-anchor='middle'%3EP%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Nunito+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap">
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
    <a href="/" class="nav-logo">Patrick Severs</a>
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
      <span>Set in Caveat and Nunito Sans. Every figure on this site has a date. Revised September 2026.</span>
      <button type="button" class="theme-toggle" data-theme-toggle>Dark mode</button>
    </div>
    <div class="footer-meta">
      <span>&copy; 2026 Patrick Severs</span>
      <span>Spring Hill, Tennessee</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
<script src="assets/js/riso.js" defer></script>
</body>
</html>
'''


PLATE_IMG = re.compile(r'<img src="assets/images/plates/plate-([a-m])\.jpg"[^>]*>')

def animate_plates(body):
    """Where src/assets/video/plate-<x>.mp4 exists, wrap the plate image in a muted looping video.
    The JPEG stays the poster and the fallback content, so the still remains the source of truth."""
    def swap(m):
        L = m.group(1)
        if not (OUT/"assets"/"video"/f"plate-{L}.mp4").exists(): return m.group(0)
        return (f'<video autoplay muted loop playsinline preload="metadata" disablepictureinpicture disableremoteplayback '
                f'poster="assets/images/plates/plate-{L}.jpg" width="1400" height="933">'
                f'<source src="assets/video/plate-{L}.webm" type="video/webm"><source src="assets/video/plate-{L}.mp4" type="video/mp4">'
                f'{m.group(0)}</video>')
    return PLATE_IMG.sub(swap, body)


for fn, (title, desc, _) in PAGES.items():
    body = animate_plates((S/"pages"/fn).read_text())
    (OUT/fn).write_text(head(fn, title, desc) + nav(fn) + body + FOOTER)
    print("wrote", fn)
