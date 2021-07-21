#!/usr/bin/python3
# rfile
# from file:///home/rfile/python3/bpvitals/bpstat09sqlite.ipynb sort of...
import logging
import sys
import pandas as pd
from datetime import *
import re
import sqlite3
from icecream import ic


def main(filename):
    try:

        engstr = "/home/rfile/python3/bpvitals/vitals.db"
        con = sqlite3.connect(engstr)
        mycurs = con.cursor()
        # log
        logger = logging.getLogger("dev")
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler("/home/rfile/python3/bin/log/weightlite.log")
        fileHandler.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        formatter = logging.Formatter(
            "%(asctime)s  %(name)s  %(levelname)s: %(message)s"
        )
        fileHandler.setFormatter(formatter)
        # log
        # read file
        wtdata = pd.read_csv(filename)
        wtdata.rename(columns={"Time": "ftime"}, inplace=True)
        # wtdata["ftime"] = pd.to_datetime(wtdata["ftime"], format="%Y/%M/%d %H:%m")
        wtdata["ftime"] = pd.to_datetime(wtdata["ftime"])
        listdate = wtdata["ftime"]
        #  strip off seconds and store to put back after other conversions  #
        # for l in listdate:
        listdate = [datetime.strftime(l, "%Y-%m-%d %H:%M") for l in listdate]
        ic(wtdata.ftime)
        ic(listdate)
        # ALTER SEQUENCE fatty_wtid_seq RESTART WITH 10
        wtdata.columns = wtdata.columns.str.lower()
        wtdata.columns = wtdata.columns.str.replace(" ", "_")
        wtdata.columns = wtdata.columns.str.replace("-", "_")
        wtdata = wtdata.replace(to_replace="\s\D*", value="", regex=True)
        wtdata.ftime = listdate
        wtdata[
            [
                "weight",
                "bmi",
                "body_fat",
                "fat_free_body_weight",
                "subcutaneous_fat",
                "visceral_fat",
                "body_water",
                "muscle_mass",
                "skeletal_muscles",
                "bone_mass",
                "protein",
                "bmr",
            ]
        ] = wtdata[
            [
                "weight",
                "bmi",
                "body_fat",
                "fat_free_body_weight",
                "subcutaneous_fat",
                "visceral_fat",
                "body_water",
                "muscle_mass",
                "skeletal_muscles",
                "bone_mass",
                "protein",
                "bmr",
            ]
        ].apply(
            pd.to_numeric
        )
        wtdata = wtdata.sort_values("ftime")
        wtdata.to_sql("qfatty", con, if_exists="append", index=False)
        logger.info("query ran on sqlite : %s ", filename)
    except Exception as e:
        print("sorry, an error occurred  ", e)
        logger.error("sqlite error:  %s", filename)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        # main("file:///home/rfile/motog3/Bob - Export Data 5-30-2021 ~ 7-19-2021.csv")
        main("file:///home/rfile/motog3/Bob - Export Data 7-17-2021 ~ 7-18-2021.csv")

