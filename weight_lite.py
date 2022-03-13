#! /usr/bin/env python3
# rfile
# from file:///home/rfile/python3/notebooks/bpinfo/weight.ipynb
import logging
import sys
import pandas as pd
from datetime import *
import re
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import DATETIME
from icecream import ic


def main(filename):
    try:

        engstr = "sqlite:////data/sqlite/vitals.db"
        eng = create_engine(engstr)
        myconn = eng.connect()
        # log
        logger = logging.getLogger("dev")
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler("/data/sqlite/weight.log")
        fileHandler.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        formatter = logging.Formatter(
            "%(asctime)s  %(name)s  %(levelname)s: %(message)s"
        )
        fileHandler.setFormatter(formatter)
        # log
        # read file
        wtdata = pd.read_csv(filename)
        # ic(wtdata)
        # wtdata.Time = wtdata.rename({"Time": "ftime"})
        # wtdata = change_column_names(wtdata, "Time", "ftime")
        wtdata.rename(columns={"Time": "ftime"}, inplace=True)
        # wtdata.ftime = pd.to_datetime(wtdata.ftime)
        # wtdata.ftime = pd.to_datetime(wtdata.ftime).strftime("%m/%d/%Y %H:%M")
        # pd.to_datetime(t).strftime("%m/%d/%Y %H:%M")

        wtdata["ftime"] = pd.to_datetime(wtdata["ftime"])

        # wtdata.ftime = pd.to_datetime(wtdata.ftime).datetime.strftime(
        #    wtdata.ftime, "%Y-%mT%h:%m")
        # wtdata.ftime = wtdata.ftime.date.strftime("YYYY-MM-DD HH:MM")
        # for t in wtdata.ftime:
        #    t = date.strftime(t, "%Y-%mT%h:%m")

        # listtime = wtdata.ftime
        ic(wtdata.ftime)
        # ALTER SEQUENCE fatty_wtid_seq RESTART WITH 10
        wtdata.columns = wtdata.columns.str.lower()
        wtdata.columns = wtdata.columns.str.replace(" ", "_")
        wtdata.columns = wtdata.columns.str.replace("-", "_")
        # this one working
        # store time data in var to put it back after replace statement below - easier than iterate through the columns
        # which had to be done to get the float data
        # listtime = DATETIME(wtdata.time)
        # listtime = wtdata.time = pd.to_datetime(wtdata.time)

        wtdata = wtdata.replace(to_replace="\s\D*", value="", regex=True)
        # wtdata.ftime = listtime  # time back in proper format for sql import
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
        wtdata.to_sql("fatty", myconn, if_exists="append", index=False)
        logger.info("query ran on sqlite : %s ", filename)
    except Exception as e:
        print("sorry, an error occurred  ", e)
        logger.error("sqlite error:  %s", filename)


def change_column_names(as_pandas, old_name, new_name):
    as_pandas.rename(columns={old_name: new_name}, inplace=True)
    return as_pandas


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        # main("file:///home/rfile/motog3/Bob - Export Data 7-20-2021 ~ 7-24-2021.csv")
        main("file:///home/rfile/motog5/Bob_export_data_dummy.csv")
