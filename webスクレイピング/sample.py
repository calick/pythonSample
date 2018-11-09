# coding: UTF-8
# import urllib2
import requests as req
import requests
import argparse
from bs4 import BeautifulSoup

print("------------- sample web scraiping -------------")

# 指定のURLから全てのリンクを取得する処理
url = "https://www.yahoo.co.jp/"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
url_items = soup.find_all('a')
print("a = ", url_items)


for url in url_items:
    res = req.urlopen(url.get("href"))
    soup = BeautifulSoup(res, 'html.parser')
    title1 = soup.find('title')
    print("title = ", title1)
    description = soup.select('item')
    print("item = ", description)
    price1 = soup.select('#price')
    print("price = ", price1)