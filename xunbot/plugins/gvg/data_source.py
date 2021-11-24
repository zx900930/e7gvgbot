import json
import requests
import os
import re
import datetime
from os import listdir

def get_todaytime():
    now_time = datetime.datetime.now()
    yesterday = now_time - datetime.timedelta(days=1)
    beforeyes = now_time - datetime.timedelta(days=2)
    weekday1 = ("1", "3", "5")
    weekday2 = ("2", "4", "6")
    # print(now_time)
    year, week_num, day_of_week = now_time.isocalendar()
    day_of_week = str(day_of_week)
    # print("day of week" + day_of_week)
    if day_of_week in weekday1:
        # print("weekday1")
        today_time = (
            "./gvgdata/" + datetime.datetime.strftime(now_time, "%Y-%m-%d") + ".txt"
        )
    elif day_of_week in weekday2:
        # print("weekday2")
        today_time = "./gvgdata/" + yesterday.strftime("%Y-%m-%d") + ".txt"
        print("当前数据文件:"+today_time)
    else:
        print("weekend")
        today_time = "./gvgdata/" + beforeyes.strftime("%Y-%m-%d") + ".txt"
        print("当前数据文件:"+today_time)
    return today_time


async def get_adv(gvg: str) -> str:
    finish = ""
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg = gvg.replace("\r", "\\r")
        gvg = gvg.replace("\n", "\\n")
        gvg_datafile.write("对方公会名称：" + gvg + "\n")
        finish = "finish"
    return finish


async def get_top(gvg: str) -> str:
    finish = ""
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg = gvg.replace("\r", "\\r")
        gvg = gvg.replace("\n", "\\n")
        gvg_datafile.write("上路 情报：\\r\\n" + gvg + "\n")
        finish = "finish"
    return finish


async def get_mid(gvg: str) -> str:
    finish = ""
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg = gvg.replace("\r", "\\r")
        gvg = gvg.replace("\n", "\\n")
        gvg_datafile.write("中路 情报：\\r\\n" + gvg + "\n")
        finish = "finish"
    return finish


async def get_bottom(gvg: str) -> str:
    finish = ""
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg = gvg.replace("\r", "\\r")
        gvg = gvg.replace("\n", "\\n")
        gvg_datafile.write("下路 情报：\\r\\n" + gvg + "\n")
        finish = "finish"
    return finish


async def get_stronghold(gvg: str) -> str:
    finish = ""
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg = gvg.replace("\r", "\\r")
        gvg = gvg.replace("\n", "\\n")
        gvg_datafile.write("主城 情报：\\r\\n" + gvg + "\n")
        finish = "finish"
    return finish


async def get_tower(gvg: str) -> str:
    finish = ""
    gvg_data = gvg.split(" ", 1)
    tower_id = gvg_data[0]
    gvg_info = gvg_data[1].lstrip()
    gvg_info = gvg_info.replace("\r", "\\r")
    gvg_info = gvg_info.replace("\n", "\\n")
    current_datafile = get_todaytime()
    with open(current_datafile, "a", encoding="utf-8") as gvg_datafile:
        time1 = datetime.datetime.now()
        time1_string = datetime.datetime.strftime(time1, "%Y-%m-%d %H:%M:%S")
        gvg_datafile.write("小塔" + tower_id + " 情报：\\r\\n" + gvg_info + "\n")
        finish = "finish"
    return finish


async def get_gvg(gvg: str) -> str:
    repass = []
    keywords = ["adv", "对手", "公会", "對手", "公會", "今天打"]
    if gvg in keywords:
        gvg = "对方公会名称"
    current_datafile = get_todaytime()
    with open(current_datafile, "r", encoding="utf-8") as gvg_datafile:
        for line in gvg_datafile:
            if re.search(r"\b" + gvg + r"\b", line):
                repass.append(line.rstrip())
    response = "\n".join(repass)
    return response


async def get_history(gvg: str) -> str:
    repass = []
    filename = ""
    for filename in listdir("./gvgdata"):
        with open("./gvgdata/" + filename, "r", encoding="utf-8") as gvg_datafile:
            for line in gvg_datafile:
                if gvg in line:
                    repass.append(line.rstrip())
    response = "\n".join(repass)
    return response
