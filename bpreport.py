#! /home/rfile/.local/share/virtualenvs/bpvitals-z9m9Wh3n/bin/python3
# /usr/bin/env python3

import pandas as pd
import numpy as np

# TODO: get rid of some extra imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.units import inch

from sqlalchemy.sql import text

eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()

bp8days = "SELECT bpdate ,bpsys AS systolic, bpdia AS diastolic, bphr AS pulse , bpsugar as glucose, ketone, bpcomment as comment from  vsigns_bp where bpdate > (SELECT date('now','-30 day'))"
bpdf = pd.read_sql_query(
    bp8days,
    myconn,
)
bpdf.columns = [
    "DATE",
    "SYSTOLIC",
    "DIASTOLIC",
    "PULSE",
    "GLUCOSE",
    "KETONE",
    "COMMENT",
]
bpsession = sessionmaker(bind=eng)
bps1 = bpsession()
exe = myconn.execute(text(bp8days))  # executing the query
result = exe.fetchall()
stylesheet = getSampleStyleSheet()
normalStyle = stylesheet["Normal"]
h2 = ParagraphStyle("ListStyle")
bt = ParagraphStyle("BodyText")

style_general = ParagraphStyle(
    name="left",
    parent=stylesheet["Normal"],
    fontSize=12,
    fontName="Helvetica",
    width="90",
    alignment=TA_LEFT,
    leading=12,
    leftIndent=0,
)

stylesheet = getSampleStyleSheet()
headingStyle = stylesheet["Heading3"]
h = Paragraph("Economic Components", headingStyle)


data = bpdf.values.tolist()
# Add the row heading to the list of lists
data.insert(0, bpdf.columns.tolist())
c1 = Canvas("test.pdf", pagesize=letter)
GRID_STYLE = TableStyle(
    [
        ("GRID", (0, 0), (-1, -1), 0.25, colors.green),
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        ("FONTNAME", (0, 0), (-1, 0), "Courier"),
        ("FONTSIZE", (0, 0), (-1, 0), 6),
    ],
)

tstx = "Blood Pressure table approx 30 days"
drugtxtpm = "Night Atenolol 50mg Losartan 100mg Triamterene hctz 37.5 25"
drugtxtam = "Day xarelto 20 mg Glimepiride 4mg EBN3 Losartan 100mg"
drugcurr = "currently taking EBN3 glimepiride in am  losartan atenolol at night"
s1p = Paragraph(tstx, style_general)
s2p = Paragraph(drugtxtpm, style_general)
s3p = Paragraph(drugtxtam, style_general)
s4p = Paragraph(drugcurr, style_general)

t1 = Table(data)
t1.setStyle(GRID_STYLE)
t1.wrapOn(c1, 100, 400)
t1.drawOn(c1, 10, 400)

# s1p.wrapOn(c1,30,700)
# s1p.drawOn(c1,50, 700)
s1p.wrapOn(c1, 300, 700)
s1p.drawOn(c1, 50, 700)
# drug pm
s2p.wrapOn(c1, 200, 200)
s2p.drawOn(c1, 50, 330)
# drug am
s3p.wrapOn(c1, 100, 400)
s3p.drawOn(c1, 50, 270)
# currently taking
s4p.wrapOn(c1, 200, 400)
s4p.drawOn(c1, 20, 200)


c1.save()

print("done")
