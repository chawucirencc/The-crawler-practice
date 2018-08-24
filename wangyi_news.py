#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import requests
import pandas as pd
import re


def gehtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error')

def getContent(html):
    arurl = re.findall(r'"url":"(.*?)",', html)
    title = re.findall(r'"title":"(.*?)",', html)
    time = re.findall(r'"time":"(.*?)",', html)
    number = re.findall(r'"comment":\'(.*?)\',', html)
    keyword = re.findall(r' "keyword":\'(.*?)\'', html)
    d = {'地址':arurl, '标题':title, '时间':time, '人数':number, '关键词':keyword}
    return d

def saveResule(dic):
    result = pd.DataFrame(dic)
    result.to_csv(r'C:\\Users\\Talent\\Desktop\\result_1.csv', encoding='gb18030', index=False)
    return

def main():
    url = 'http://data.163.com/special/datablog/'
    html = gehtmlText(url)
    dic = getContent(html)
    saveResule(dic)

main()
