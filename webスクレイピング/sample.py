# coding: UTF-8
# import urllib2
import requests
import argparse
from bs4 import BeautifulSoup

print("sample web scraiping")

# アクセスするURL
# url = "http://www.nikkei.com/"
url = "https://www.yahoo.co.jp/"

# URL取得
# html = urllib2.urlopen(url)
html = requests.get(url)

# get title
soup = BeautifulSoup(html.content, "html.parser")
print("title : " + soup.title.string)

# 特定のタグの情報を集める
lis = soup.find_all("li")
for li in lis:
    print(li.string)


# f=open('test.html','w')
# f.write(soup.title.string)
# f.close()

print("end")

