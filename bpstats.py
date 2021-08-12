#!/usr/bin/env python3

# rfile
# from file:///home/rfile/python3/notebooks/bpinfo/bpstat09pg.ipynb
import dateutil.parser
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import select
import matplotlib.pyplot as plt
from matplotlib import cbook, dates
import mplcursors

eng = create_engine("sqlite:////data/sqlite/vitals.db")
myconn = eng.connect()
# get data for sugar
# this one now working and showing 2 subplots Saturday, June 5, 2021 10:57:39 AM EDT
# never got cursor to work so added mplcursors lib
# get data
sugeightdays = (
    "SELECT bsdate,bsugar FROM qtsugar WHERE bsdate > (SELECT date('now','-8 day'))"
)
sugar8days = pd.read_sql_query(sugeightdays, myconn, parse_dates="bsdate")
sugar8days = sugar8days.sort_values("bsdate")
fig3, ax3, = plt.subplots(1, 2)
plt.subplot(1, 2, 1)
# start setting up figure
mylegend = "7 days stats "
mystats = sugar8days.describe(include="int")
plt.ylim(60, 150)
ax3[0].set_xlabel("Date")
plt.title("blood sugar last 8 days")
ax3[0].annotate([mystats], xy=(200, 380), xycoords="figure points")
plt.setp(ax3[0].get_xticklabels(), rotation=90, fontsize=6)
# ax3.set_xticklabels(sugar8days.bsdate, rotation=90, fontsize=6)
plt.grid(
    b=True, which="both", axis="both",
)
fig3.set_figwidth(15)
fig3.set_figheight(10)
# thetable = pd.plotting.table(fig3, sugar8days, colLabels= sugar8days.columns )
lines = ax3[0].plot(
    sugar8days.bsdate, sugar8days.bsugar, marker="o", linestyle="dashed"
)
plt.subplot(1, 2, 2)
plt.table(
    cellText=sugar8days.values,
    colWidths=[0.25] * len(sugar8days.columns),
    rowLabels=None,
    colLabels=sugar8days.columns,
    cellLoc="center",
    rowLoc="center",
    loc="center",
)
mplcursors.cursor(lines)  # or just mplcursors.cursor()
# plt.show()


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


plt.show()

