

# rfile
# from file:///home/rfile/python3/notebooks/bpinfo/bpstat09pg.ipynb
# import dateutil.parser
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import mplcursors

eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()

def days7():
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
    #plt.draw()
    # myconn.close()
    plt.show()
def bp7days():
    # blood pressure data 7 days
    bpsevendays = "SELECT bpdate ,bpsys AS systolic, bpdia AS diastolic, bphr AS pulse from  vsigns_bp where bpdate > (SELECT date('now','-7 day'))"
    bp7days = pd.read_sql_query(bpsevendays, myconn, parse_dates="bpdate")
    # bar chart blood pressure
    x = np.arange(len(bp7days))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(
        x - width / 2, bp7days.systolic, width, label="systolic", facecolor="#00388F"
    )
    rects2 = ax.bar(
        x + width / 2, bp7days.diastolic, width, label="diastolic", facecolor="#8F5600"
    )
    rects3 = ax.bar(x + width, bp7days.pulse, width, label="pulse", facecolor="#638F00")
    ax.axhline(y=120, color="#00388F")
    ax.axhline(y=80, color="#8F5600")
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("120/80 = perfect")
    ax.set_title("Blood press 7 days")
    ax.set_xticks(x)
    ax.set_xticklabels(bp7days.bpdate, rotation=90, fontsize=6)
    ax.legend()

    ax.bar_label(rects1, label_type="center", color="#EEEED0")
    ax.bar_label(rects2, label_type="center")
    ax.bar_label(rects3, label_type="center")
    plt.rc("xtick", labelsize=6)
    fig.set_figheight(10)
    mplcursors.cursor(rects3)
    mplcursors.cursor(rects2)
    plt.show()  # draw?
    #fig.canvas.draw()
    


def sugar48():
    sugonedays = "SELECT bsdate,bsugar FROM qtsugar WHERE bsdate >= (SELECT date('now', '-48 hours'))"
    sugar1days = pd.read_sql_query(sugonedays, myconn, parse_dates="bsdate")
    plot = sugar1days.plot.line(x="bsdate", y="bsugar",  title="sugar 48 hours")
    plt.tight_layout()
    plt.show()


    
   
        
        