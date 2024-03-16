#! /home/rfile/.local/share/virtualenvs/bpvitals-z9m9Wh3n/bin/python3
# /usr/bin/env python3

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
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import array
eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()

bp8days = "SELECT bpdate ,bpsys AS systolic, bpdia AS diastolic, bphr AS pulse , bpsugar as glucose, ketone, bpcomment as comment from  vsigns_bp where bpdate > (SELECT date('now','-30 day'))"
bpdf = pd.read_sql_query(bp8days, myconn, )
bpdf.columns =["DATE" , "SYSTOLIC", "DIASTOLIC", "PULSE", "GLUCOSE", "KETONE", "COMMENT"]
bpsession = sessionmaker(bind=eng)
bps1 = bpsession()
exe = myconn.execute(text(bp8days)) #executing the query
result = exe.fetchall() 
stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Normal']
data = bpdf.values.tolist()
# Add the row heading to the list of lists
data.insert(0, bpdf.columns.tolist())
c1 = Canvas('bpreport.pdf', pagesize=letter)
GRID_STYLE = TableStyle(
            [('GRID', (0, 0), (-1, -1), 0.25, colors.green),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            
            ('FONTSIZE', (0,0), (-1,0), 8)])
t1 = Table(data)
t1.setStyle(GRID_STYLE) 
t1.wrapOn(c1, 10, 400)
t1.drawOn(c1, 10, 400)
c1.save()
print('done')


