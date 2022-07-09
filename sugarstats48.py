#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:49:20 2022

@author: rfile
"""
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()
def displaysugar():
    sugonedays = "SELECT bsdate,bsugar FROM qtsugar WHERE bsdate >= (SELECT date('now', '-48 hours'))"
    sugar1days = pd.read_sql_query(sugonedays, myconn, parse_dates="bsdate")
    plot = sugar1days.plot.line(x="bsdate", y="bsugar",  title="sugar 48 hours")
    plt.tight_layout()
    plt.show()
    myconn.close()
