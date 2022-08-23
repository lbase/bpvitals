import pandas as pd
import pdfkit as pdf
import sqlite3

con=sqlite3.connect("/data/sqlite/vitals.db")
sqlquery = """select bpdate as "date",
bpsys as "systolic", 
bpdia as "diastolic"  ,  
bphr as "hr" ,
bpoxy as "O2" , 
bpsugar as "sugar" , 
bpcomment as "comment"
from vsigns_bp  where bpdate >= '2022-07-01 01:00' and bpdate <= '2022-08-20 01:00'"""
# orig where bpdate >= '2022-07-01 01:00'
df=pd.read_sql_query(sqlquery, con)
df.to_html('/home/rfile/python3/bpvitals/bpress_f.html')
mypdf = '/home/rfile/python3/bpvitals/bpress_f.pdf'
pdf.from_file('/home/rfile/python3/bpvitals/bpress_f.html', mypdf)
