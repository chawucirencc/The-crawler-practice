#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import re
import requests
import pandas as pd
import time


def getUrl(url, u):
    """通过循环得到URL列表"""
    for i in range(0, 40, 2):
        new_url = url + str(i*10)
        u.append(new_url)
    return u

def getPage(uinfo, ulist):
    """将列表中的URL的源代码保存到一个字符串当中"""
    for s in ulist:
        try:
            r = requests.get(s)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            uinfo = r.text + uinfo
        except:
            print('error')
        time.sleep(3)
    return uinfo

def getContent(parse):
    """通过正则表达式爬取到想要得到的消息"""
    title = re.findall(r'"title":"(.*?)"', parse)
    address = re.findall(r'"url":"(.*?)"', parse)
    rate = re.findall(r'"rate":"(.*?)"', parse)
    return title, address, rate


def saveResule(result):
    """用DataFrame将结果保存到文件"""
    d = {'电影名称':result[0], '电影地址':result[1], '电影评分': result[2]}
    end_data = pd.DataFrame(d)
    end_data.to_csv(r'relt.csv', encoding='gb18030', index=False)
    return

def main():
    """主函数"""
    base_url = 'https://movie.douban.com/j/search_subjects?'
    params = 'type=movie&tag=豆瓣高分&sort=rank&page_limit=20&page_start='
    url = base_url + params
    u = []
    ulist = getUrl(url, u)
    uinfo = ''
    parse = getPage(uinfo, ulist)
    result = getContent(parse)
    saveResule(result)


main()
