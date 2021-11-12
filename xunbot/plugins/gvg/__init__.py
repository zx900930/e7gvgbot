from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import thulac

from ...hanziconv import HanziConv
from ...xlog import xlogger
from xunbot import get_bot

import re
import time

from .data_source import (
    get_gvg,
    get_top,
    get_mid,
    get_bottom,
    get_stronghold,
    get_tower,
    get_history,
    get_adv,
)

__plugin_name__ = '团战助手'
__plugin_usage__ = r"""
第七史诗团战助手使用说明:
1.输入情报: 格式为 助手 上路/中路/下路/主城/小塔
2.查询情报: 格式为 助手 情报
3.历史记录: 格式为 助手 历史
4.团战汇报工具： https://triatk.gitee.io/epicseven/
5.还有一些团战无关的功能请用: 助手 帮助
""".strip()

def wrap(text, lenth):
    textArr = re.findall(".{" + str(lenth) + "}", text)
    textArr.append(text[(len(textArr) * lenth) :])
    return textArr


@on_command("gvghelp", aliases=("团战帮助", "团战说明"), permission=get_bot().level)
async def help(session: CommandSession):
    helpinfo = "使用说明:\r\n1.输入情报: 格式为 助手 上路/中路/下路/主城/小塔\
                         \r\n2.查询情报: 格式为 助手 情报 \
                         \r\n3.历史记录: 格式为 助手 历史\
                         \r\n4.团战汇报工具： https://triatk.gitee.io/epicseven/\
                         \r\n5.还有一些团战无关的功能请用: 助手 帮助"
    await session.send(helpinfo)


@on_command("gvghelpen", aliases=("gvghelp", "gvgh"), permission=get_bot().level)
async def helpen(session: CommandSession):
    helpinfo = "Command List:\r\n1.Input information:  gvg top/mid/bottom/stronghold/tower\
                             \r\n2.Query information: gvg info \
                             \r\n3.History: gvg history\
                             \r\n4.Others(No English version)"
    await session.send(helpinfo)


@on_command(
    "adv", aliases=("adv", "对手", "公会", "對手", "公會", "今天打"), permission=get_bot().level
)
async def adv(session: CommandSession):
    adv_data_report = ""
    adv_data = session.get("adv", prompt="请输入对方公会名称, 重复输入为覆盖")
    adv_data_report = await get_adv(adv_data)
    if adv_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("top", aliases=("top", "上路"), permission=get_bot().level)
async def top(session: CommandSession):
    top_data_report = ""
    top_data = session.get("top", prompt="请输入情报")
    top_data_report = await get_top(top_data)
    top_data_report = top_data_report.replace("\\r", "\r")
    top_data_report = top_data_report.replace("\\n", "\n")
    # for line in top_data_report.splitlines():
    #     line = line.rstrip("\r\n")
    if top_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("mid", aliases=("mid", "中路"), permission=get_bot().level)
async def mid(session: CommandSession):
    mid_data_report = ""
    mid_data = session.get("mid", prompt="请输入情报\r\n团战汇报工具： https://triatk.gitee.io/epicseven/")
    mid_data_report = await get_mid(mid_data)
    mid_data_report = mid_data_report.replace("\\r", "\r")
    mid_data_report = mid_data_report.replace("\\n", "\n")
    # for line in mid_data_report.splitlines():
    #     line = line.rstrip("\r\n")
    if mid_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("bottom", aliases=("bottom", "下路"), permission=get_bot().level)
async def bottom(session: CommandSession):
    bottom_data_report = ""
    bottom_data = session.get("bottom", prompt="请输入情报\r\n团战汇报工具： https://triatk.gitee.io/epicseven/")
    bottom_data_report = await get_bottom(bottom_data)
    bottom_data_report = bottom_data_report.replace("\\r", "\r")
    bottom_data_report = bottom_data_report.replace("\\n", "\n")
    # for line in bottom_data_report.splitlines():
    #     line = line.rstrip("\r\n")
    if bottom_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("stronghold", aliases=("stronghold", "主城"), permission=get_bot().level)
async def stronghold(session: CommandSession):
    stronghold_data_report = ""
    stronghold_data = session.get("stronghold", prompt="请输入情报\r\n团战汇报工具： https://triatk.gitee.io/epicseven/")
    stronghold_data_report = await get_stronghold(stronghold_data)
    stronghold_data_report = stronghold_data_report.replace("\\r", "\r")
    stronghold_data_report = stronghold_data_report.replace("\\n", "\n")
    # for line in stronghold_data_report.splitlines():
    #     line = line.rstrip("\r\n")
    if stronghold_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("tower", aliases=("tower", "小塔"), permission=get_bot().level)
async def tower(session: CommandSession):
    tower_data_report = ""
    tower_data = session.get(
        "tower",
        prompt="请输入小塔情报，格式为：小塔编号(纯数字，不要在前面加上下路之类) 情报内容\r\n小塔编号从左往右 上路1-8 中路11-18 下路21-28\r\n例子： 4 p1 埃及速度最多280 p2 200+速度 22k血金刚石暗龙，反击大宝剑龟速老头15k血， 150速左右尘埃凯隆  作业:宝马 光玛雅 火奶\r\n团战汇报工具： https://triatk.gitee.io/epicseven/",
    )
    tower_data_report = await get_tower(tower_data)
    tower_data_report = tower_data_report.replace("\\r", "\r")
    tower_data_report = tower_data_report.replace("\\n", "\n")
    # for line in tower_data_report.splitlines():
    #     line = line.rstrip("\r\n")
    if tower_data_report:
        await session.send("保存成功")
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("gvg", aliases=("info", "情报", "情報"), permission=get_bot().level)
async def gvg(session: CommandSession):
    gvg_data = session.get(
        "gvg",
        prompt="请输入目标: 上路 中路 下路 主城 \r\n小塔请直接输入小塔+编号 例子：小塔1 小塔2 小塔24\r\n小塔编号从左往右 上路1-8 中路11-18 下路21-28(小塔编号为纯数字，使用时不要在前面加上下路)\r\n输入 对手/公会/今天打 查询今日对手\r\n伤害计算器： https://triatk.gitee.io/maphe.github.io/zh/",
    )
    gvg_data_report = ""
    gvg_data_report = await get_gvg(gvg_data)
    print("1" + gvg_data_report)
    reply = gvg_data + " 情报："
    keywords = ["adv", "对手", "公会", "對手", "公會", "今天打"]
    if gvg_data in keywords:
        gvg_data = "对方公会名称"
        reply = "对方公会名称："
    print(reply)
    gvg_data_head = gvg_data[0:5]
    gvg_data_head = str(gvg_data_head)
    if gvg_data == "top":
        gvg_data = "上路"
        reply = "Top info:"
    if gvg_data == "mid":
        gvg_data = "中路"
        reply = "Mid info:"
    if gvg_data == "bottom":
        gvg_data = "下路"
        reply = "Bottom info:"
    if gvg_data == "stronghold":
        gvg_data = "主城"
        reply = "Stronghold info:"
    if gvg_data_head == "tower":
        tower_number = gvg_data[6, -1]
        tower_number = str(tower_number)
        print(type(tower_number))
        print(tower_number)
        gvg_data = "小塔" + tower_number
        reply = "Tower" + tower_number + " info:"
    gvg_data_report = re.sub(reply, "", gvg_data_report)
    gvg_data_report = gvg_data_report.replace("\\r", "\r")
    gvg_data_report = gvg_data_report.replace("\\n", "\n")
    gvg_data_report = reply + gvg_data_report
    print(type(gvg_data_report))
    print("2" + gvg_data_report)
    if gvg_data_report:
        await session.send(gvg_data_report)
    else:
        await session.send("[ERROR]无法获得对应的情报")


@on_command("history", aliases=("history", "历史", "歷史"), permission=get_bot().level)
async def history(session: CommandSession):
    history_data_report = ""
    gvg_data = session.get("gvg", prompt="要搜索的内容: 可以为任意关键字")
    history_data_report = await get_history(gvg_data)
    # history_data_report = history_data_report.replace("\\r\\n", "\r\n")
    if history_data_report:
        await session.send(history_data_report)
    else:
        await session.send("[ERROR]无法获得对应的情报")


@adv.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["adv_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("对手名称不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@top.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["top_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@mid.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["mid_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@bottom.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["bottom_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@stronghold.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["stronghold_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@tower.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["tower_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@gvg.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["gvg_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报目标不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


@history.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state["history_data"] = stripped_arg
        return

    if not stripped_arg:
        session.pause("情报目标不能为空，请重新输入")

    session.state[session.current_key] = stripped_arg


# @on_natural_language(keywords={'top', '上路'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'top', current_arg=msg or '')

# @on_natural_language(keywords={'mid', '中路'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'mid', current_arg=msg or '')

# @on_natural_language(keywords={'bottom', '下路'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'bottom', current_arg=msg or '')

# @on_natural_language(keywords={'stronghold', '主城'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'stronghold', current_arg=msg or '')

# @on_natural_language(keywords={'tower', '小塔'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'tower', current_arg=msg or '')

# @on_natural_language(keywords={'gvg', '情报','情報'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'gvg', current_arg=msg or '')

# @on_natural_language(keywords={'history', '历史','歷史'}, permission=get_bot().level)
# async def _(session: NLPSession):
# msg = session.msg

# return IntentCommand(90.0, 'history', current_arg=msg or '')

