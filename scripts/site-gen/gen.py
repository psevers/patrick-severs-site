import sys, pathlib
S = pathlib.Path(__file__).parent
OUT = pathlib.Path(__file__).resolve().parents[2]/"src"

PAGES = {
  "index.html": ("Patrick Severs: Head of GTM, Human Data and AI-Native Service Lines",
     "I build the AI training-data business inside your company, walk it into the frontier labs, and build the team that delivers. G2i: one staffing line to human data for frontier labs, $10-15M to a ~$80M target in three years.", "Home"),
  "gtm-leadership.html": ("The G2i Record: Patrick Severs",
     "Three years running G2i's revenue and human-data business: one staffing business to four business lines, 122% growth, margin held. The general-manager record, with the sales part inside it.", "The G2i record"),
  "human-data-operating-layer.html": ("The Human Data Operating Layer: Patrick Severs",
     "A working blueprint for building a frontier-lab human-data business inside an existing company: the operating layer, the minimum viable team, the GTM motion, the quality system, and the scoreboard.", "Operating layer"),
  "agent-company.html": ("The Agent Company, 45 days in: Patrick Severs",
     "A live GTM engagement: day one had no CRM, no lead source, and no decision on what to sell. What got built in 45 days and what it produced.", "Agent Company"),
  "how-i-operate.html": ("How I Operate: Patrick Severs",
     "Five operating rules with receipts: direct don't do, interview before you task, cost is policy, a human approves every send, presence beats outbound. Plus the agent fleet and the tools built under my direction.", "How I operate"),
  "career.html": ("Career: Patrick Severs",
     "Twenty-five years from carrying a bag at Dell to running revenue and human data at G2i. The shape of it, era by era.", "Career"),
}

NAV_ITEMS = [
  ("index.html", "Home"),
  ("gtm-leadership.html", "The G2i record"),
  ("human-data-operating-layer.html", "Operating layer"),
  ("agent-company.html", "Agent Company"),
  ("how-i-operate.html", "How I operate"),
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&family=Caveat:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <marker id="wb-arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="var(--ink)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <marker id="wb-arrowhead-accent" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1,1 L9,5 L1,9" fill="none" stroke="var(--marker)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></marker>
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
    <a href="/" class="nav-logo">Patrick<span>.</span>Severs</a>
    <ul class="nav-links" data-nav-links>
      {items}
      <li><a href="#contact" class="nav-cta">Contact</a></li>
    </ul>
    <div class="nav-right">
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle dark mode">
        <svg class="icon-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="icon-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
      </button>
      <button class="nav-toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
</nav>
'''

FOOTER = '''<footer class="footer" id="contact">
  <div class="container">
    <div class="footer-inner reveal">
      <img src="assets/images/headshot.png" alt="Patrick Severs" class="footer-photo" loading="lazy">
      <div class="footer-text">
        <h2>Let's talk.</h2>
        <p>Building a human-data or AI-native service line and need someone to run it. Hiring a head of GTM or revenue. Or you want to talk through how the operating layer would look inside your business. Start with the resume, or skip straight to a conversation.</p>
        <div class="footer-links">
          <a href="assets/pdf/patrick-severs-resume.pdf" class="btn btn-primary" target="_blank" rel="noopener">Resume (PDF)</a>
          <a href="https://calendly.com/pvsevers/30min" class="btn btn-secondary" target="_blank" rel="noopener">Book 30 min</a>
          <a href="mailto:pvsevers@gmail.com" class="btn btn-secondary">pvsevers@gmail.com</a>
          <a href="https://www.linkedin.com/in/pvsevers/" class="btn btn-secondary" target="_blank" rel="noopener">LinkedIn</a>
          <a href="https://github.com/psevers" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
        </div>
      </div>
    </div>
    <div class="footer-meta">
      <span>&copy; 2026 Patrick Severs</span>
      <span>Spring Hill, TN</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
'''

for fn, (title, desc, _) in PAGES.items():
    body = (S/"pages"/fn).read_text()
    (OUT/fn).write_text(head(fn, title, desc) + nav(fn) + body + FOOTER)
    print("wrote", fn)
