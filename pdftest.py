import pandas as pd
import pdfkit as pdf
import sqlite3

con=sqlite3.connect("/data/sqlite/vitals.db")

df=pd.read_sql_query("select * from qtsugar where bsdate >= '2022-06-01 07:30'", con)
df.to_html('/home/rfile/python3/bpvitals/sugar.html')
mypdf = '/home/rfile/python3/bpvitals/sugar.pdf'
pdf.from_file('/home/rfile/python3/bpvitals/sugar.html', mypdf)