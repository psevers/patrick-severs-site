from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors

OUT = "src/assets/pdf/patrick-severs-resume.pdf"

ACCENT = colors.HexColor("#0a7d3e")
INK = colors.HexColor("#14161a")
INK_SOFT = colors.HexColor("#4a4f58")

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
    title="Patrick Severs - Resume",
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle("Name", fontName="Courier-Bold", fontSize=20, textColor=INK, spaceAfter=2, leading=22)
title_style = ParagraphStyle("Title", fontName="Courier", fontSize=10.5, textColor=ACCENT, spaceAfter=4, leading=13)
contact_style = ParagraphStyle("Contact", fontName="Helvetica", fontSize=9, textColor=INK_SOFT, spaceAfter=8, leading=12)
section_style = ParagraphStyle("Section", fontName="Courier-Bold", fontSize=10.5, textColor=INK, spaceBefore=10, spaceAfter=4, leading=13)
summary_style = ParagraphStyle("Summary", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=13, spaceAfter=2)
role_style = ParagraphStyle("Role", fontName="Helvetica-Bold", fontSize=9.5, textColor=INK, spaceBefore=6, spaceAfter=1, leading=12)
meta_style = ParagraphStyle("Meta", fontName="Helvetica-Oblique", fontSize=8.5, textColor=INK_SOFT, spaceAfter=3, leading=11)
bullet_style = ParagraphStyle("Bullet", fontName="Helvetica", fontSize=9, textColor=INK, leading=12.5, spaceAfter=2, leftIndent=12, bulletIndent=0)
edu_style = ParagraphStyle("Edu", fontName="Helvetica", fontSize=9, textColor=INK, leading=12, spaceAfter=2)

story = []

story.append(Paragraph("Patrick Severs", name_style))
story.append(Paragraph("Head of Revenue &amp; GTM Leader — AI-Native Companies", title_style))
story.append(Paragraph("pvsevers@gmail.com &nbsp;|&nbsp; linkedin.com/in/pvsevers &nbsp;|&nbsp; Spring Hill, TN", contact_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#dedad0"), spaceAfter=6))

story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "GTM leader with 25 years in sales and revenue leadership. Built G2i's AI-native go-to-market motion "
    "from a single staffing line into four business lines, growing revenue 122% year over year (21.7x EBITDA "
    "growth), while personally running a governed 7-agent AI fleet that operates the GTM org day to day.",
    summary_style))

story.append(Paragraph("EXPERIENCE", section_style))

def role(title_line, meta_line, bullets):
    story.append(Paragraph(title_line, role_style))
    story.append(Paragraph(meta_line, meta_style))
    for b in bullets:
        story.append(Paragraph("&bull;&nbsp; " + b, bullet_style))

role(
    "G2i Inc. — Head of Revenue &amp; Human Data; Senior Director Sales &amp; Partnerships; Director of Sales &amp; Partnerships",
    "Sep 2023 – Present &nbsp;|&nbsp; Nashville, TN",
    [
        "Grew G2i from a single staffing motion to four business lines (elite AI engineer placement, human data/RL "
        "environments for frontier labs, managed services, and Orchestrator — an agent orchestration product), "
        "taking revenue from a $10-15M base toward an $80M 2026 trajectory.",
        "Revenue grew 122% year over year with EBITDA growth of 21.7x quarter over quarter; built the first live "
        "RevOps reporting system, forecast model, and cross-functional partnership across finance, talent, and engineering.",
        "Deployed 100 engineers in under two days for a frontier lab's codex-testing project; built relationships "
        "with Microsoft, Meta, Coinbase, and Discover.",
    ],
)

role(
    "Braintrust — VP Client Development; Director of Enterprise Account Expansion",
    "Nov 2020 – Sep 2023 &nbsp;|&nbsp; Spring Hill, TN",
    ["Grew enterprise accounts for a decentralized talent network — first exposure to the AI-adjacent talent economy."],
)

role(
    "Box — Enterprise Account Executive",
    "Nov 2018 – Nov 2020 &nbsp;|&nbsp; Nashville, TN",
    ["Sold into complex enterprise accounts at a public SaaS company at scale."],
)

role(
    "ADP — Workforce Management Consultant",
    "Nov 2016 – Nov 2018 &nbsp;|&nbsp; Nashville, TN",
    ["Consultative selling of enterprise workforce management software."],
)

role(
    "ServiceSource — Senior Director, Account Management; Director of Account Management; Senior Sales Manager",
    "May 2012 – Nov 2016 &nbsp;|&nbsp; Nashville, TN",
    ["Ran renewal and expansion motions as account-management leadership, growing from managing a team to owning a function."],
)

role(
    "Dell — Financial Services Sales Manager; Inside Sales Manager; Senior Account Manager",
    "Jun 2000 – Apr 2012 &nbsp;|&nbsp; Nashville, TN",
    ["Twelve years of individual and team quota ownership, from account management through sales management. 2018 President's Club Winner."],
)

story.append(Paragraph("ADDITIONAL", section_style))
story.append(Paragraph(
    "&bull;&nbsp; Built and personally run a governed 7-agent AI fleet (own repos, CI, cost governance, security review) "
    "that operates GTM reporting, pipeline analysis, and standups.",
    bullet_style))

story.append(Paragraph("EDUCATION", section_style))
story.append(Paragraph("Tennessee State University — B.A., History &amp; American Studies (1996 – 1999)", edu_style))
story.append(Paragraph("Middle Tennessee State University — History &amp; Political Science (1992 – 1996)", edu_style))

doc.build(story)
print("wrote", OUT)
