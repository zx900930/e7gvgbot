import requests
from lxml import etree
import time

from kth_timeoutdecorator import *
from xunbot import get_bot

from ...xlog import xlogger

TIMELIMIT_ANIME = get_bot().config.TIMELIMIT_ANIME
MAXINFO_ANIME = get_bot().config.MAXINFO_ANIME


async def from_anime_get_info(key_word: str) -> str:
    repass = ""
    url = 'https://mikanani.me/Home/Search?searchstr=' + key_word
    try:
        xlogger.debug("Now starting get the {}".format(url))
        repass = await get_repass(url)
    except TimeoutException as e:
        xlogger.error("Timeout! {}".format(e))
    
    return repass

@timeout(TIMELIMIT_ANIME)
async def get_repass(url: str) -> str:
    repass = ""
    putline = []

    html_data = requests.get(url)
    html = etree.HTML(html_data.text)
    
    anime_list = html.xpath('//*[@id="sk-container"]/div[2]/table/tbody/tr')
    if len(anime_list) > MAXINFO_ANIME:
        anime_list = anime_list[:MAXINFO_ANIME]
    
    for anime in anime_list:
        # class_a = anime.xpath('./td[@width="6%"]//font/text()')[0]
        title = (anime.xpath('./td/a[@class="magnet-link-wrap"]/text()')[0]).strip()
        magent_long = anime.xpath('./td[1]/a[2]')[0].attrib['data-clipboard-text']
        magent = magent_long[:magent_long.find('&')]
        size = anime.xpath('./td[2]/text()')[0]
        putline.append("{}\n【{}】| {}".format(title, size, magent))
    
    repass = '\n\n'.join(putline)
    repass = "\n".join(repass.splitlines())
    # print(repass)
    return repass