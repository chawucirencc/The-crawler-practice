#!/usr/bin/env.python
# -*- coding: utf-8 -*-
# -*- coding:utf8 -*-
import requests
import re
from bs4 import BeautifulSoup


def getHtmlText(URL_GET, params):#
    """构建网页文本函数"""
    try:
        r = requests.get(URL_GET, params=params)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error')

def getSoup(html, uinfo):
    '''构建Soup文本函数'''
    soup = BeautifulSoup(html, 'html.parser')
    counte = soup.find_all(name='img')
    for i in counte:
        uinfo.append(re.sub('\\\\', '/', i['src'][2:-2]))
    return uinfo

def saveResult(count, imgpath):
    a = 0
    for x in count:
        rt = requests.get(x)
        rt.raise_for_status()
        print('正在下载第%d张照片...' % a)
        with open(imgpath + str(a) + '.jpg', 'wb') as f:
            f.write(rt.content)
        a += 1


def main():
    URL_GET = "https://api.douban.com/v2/event/list"  # 根网址
    params = {'loc': '108288', 'day_type': 'weekend', 'type': 'exhibition'}  # 构建类型字典
    imgpath = 'C:\\Users\\Talent\\Desktop\\file\\photo'
    html = getHtmlText(URL_GET, params)
    uinfo = []
    count = getSoup(html, uinfo)
    saveResult(count, imgpath)


main()
