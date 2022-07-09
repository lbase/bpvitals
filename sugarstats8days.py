#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 16:03:45 2022

@author: rfile
"""

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import mplcursors

eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()
def sug8days():
    # get data for sugar
    #  this one working and showing the variable mystats n
    # never got cursor to work so added mplcursors lib
    # get data
    sugeightdays = "SELECT bsdate,bsugar FROM qtsugar WHERE bsdate > (SELECT date('now','-8 day'))"
    sugar8days = pd.read_sql_query(sugeightdays, myconn, parse_dates = "bsdate")
    # start setting up figure
    mylegend = "7 days stats "
    mystats = sugar8days.describe(include='int')
    sugar8days=sugar8days.sort_values("bsdate")
    fig3, ax3 = plt.subplots()
    plt.ylim(100,250)
    ax3.set_xlabel('Date')
    plt.title('blood sugar last 8 days')
    ax3.annotate([mystats], xy=(200, 380), xycoords='figure points')
    plt.setp(ax3.get_xticklabels(), rotation = 90, fontsize=6)
    #ax3.set_xticklabels(sugar8days.bsdate, rotation=90, fontsize=6)
    plt.grid(visible=True, which='both', axis='both', )
    fig3.set_figwidth(18)
    fig3.set_figheight(9)
    lines = ax3.plot(sugar8days.bsdate , sugar8days.bsugar, marker='o', linestyle='dashed' )
    mplcursors.cursor(lines) # or just mplcursors.cursor()
    plt.show()
    myconn.close