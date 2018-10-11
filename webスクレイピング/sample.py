# coding: UTF-8
# import urllib2
import requests
import argparse
from bs4 import BeautifulSoup

print("------------- sample web scraiping -------------")

# アクセスするURL
# url = "http://www.nikkei.com/"
url = "http://db.netkeiba.com/race/201605040411/"

# URL取得
# html = urllib2.urlopen(url)
html = requests.get(url)

# get title
soup = BeautifulSoup(html.content, "html.parser")
print(soup.string)
# print("title : " + soup.title.string)

# 特定のタグの情報を集める
data = soup.find_all("h1")
print(data)
for a in data:
    # stringだとタグがあるとNoneになるのでtextとしている
    race_name=a.text
    print(race_name)

# 特定のタグの情報を集める
# classで絞る
test_string="class filter sample"
print(test_string)
td = soup.find_all("td")
for tag in td:
	try:
		string_ = tag.get("class").pop(0)
		if string_ in "txt_l":
			test_string = tag.text
			break
	except:
		# 何もしない
		pass
print(test_string)

# f=open('test.html','w')
# f.write(soup.title.string)
# f.close()

print("end")

