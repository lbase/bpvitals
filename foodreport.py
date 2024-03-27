#! /home/rfile/.local/share/virtualenvs/bpvitals-z9m9Wh3n/bin/python3

# /usr/bin/env python3

from tkinter.messagebox import YES
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
from matplotlib import cbook, dates
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import array
eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()

styles=getSampleStyleSheet()
doc = SimpleDocTemplate("foodtest.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18, )
# c1 = Canvas('foodtest.pdf', pagesize=letter)
# c1 = SimpleDocTemplate('foodtest.pdf', pagesize=letter, allowSplitting=1)


GRIDF_STYLE = TableStyle(
            [('GRID', (0, 0), (-1, -1), 0.25, colors.blue),
            ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Courier'),
            ('FONTSIZE', (0,0), (-1,0), 12),
            ])


foodinfo = "SELECT fdate, fnotes FROM foodnotes where fdate > (SELECT date('now','-30 day'))"
fooddf = pd.read_sql_query(foodinfo, myconn, )
fooddf.columns =["DATE" , "NOTES"]
# get rid of CR
# fooddf['NOTES'] = fooddf['NOTES'].str.replace('\n' , '')
colwidths_2 = [300] * (len(fooddf)+1)
rowheights_2 = [15] * (len(fooddf)+1)
food_data = fooddf.values.tolist()
food_data.insert(0, fooddf.columns.tolist())
story = []


# t2 = Table(food_data , hAlign='LEFT', repeatRows=1, splitByRow=1, splitInRow=5 )
t2 = Table(food_data , hAlign='LEFT', repeatRows=1)
t2.setStyle(GRIDF_STYLE)
story.append(t2)

# t2.wrapOn(c1, 10, 400)
# t2.drawOn(c1, 5, 50)
# t2.splitOn(c1, 100, 200)

# print(story)
doc.build(story)

print('done')
