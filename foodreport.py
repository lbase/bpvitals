#! /home/rfile/.local/share/virtualenvs/bpvitals-z9m9Wh3n/bin/python3
# read
# /usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.units import inch


eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()

styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    "foodtest.pdf",
    pagesize=letter,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=18,
)


GRIDF_STYLE = TableStyle(
    [
        ("GRID", (0, 0), (-1, -1), 0.25, colors.blue),
        ("ALIGN", (1, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Courier"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
    ]
)

# regular query
foodinfo = (
    "SELECT fdate, fnotes FROM foodnotes where fdate > (SELECT date('now','-30 day'))"
)
#diarrhea query
#foodinfo = ("SELECT fdate, fnotes FROM foodnotes where fdate > (SELECT date('now','-30 day')) AND fnotes LIKE '%diarrhea%' ")

fooddf = pd.read_sql_query(
    foodinfo,
    myconn,
)
fooddf.columns = ["DATE", "NOTES"]
# get rid of CR
# fooddf['NOTES'] = fooddf['NOTES'].str.replace('\n' , '')
colwidths_2 = [300] * (len(fooddf) + 1)
rowheights_2 = [15] * (len(fooddf) + 1)
food_data = fooddf.values.tolist()
food_data.insert(0, fooddf.columns.tolist())
story = []
t2 = Table(food_data, hAlign="LEFT", repeatRows=1)
t2.setStyle(GRIDF_STYLE)
story.append(t2)
doc.build(story)

print("done")
