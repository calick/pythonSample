# coding: UTF-8
from bs4 import BeautifulSoup
import re

# file_path="race/201205040911.html"
file_path="race/201805050403.html"

html = open(file_path,"r")
soup = BeautifulSoup(html,"html.parser")

title = re.split('[｜|]',soup.title.string)
### レース名 ###
print("race_name : " + title[0])
### 開催日 ###
print("race_date : " + title[1])

xml = soup.select('dl[class^="racedata fc"]')
### 何レース目か？ ###
print("race_number : " + xml[0].dt.string.strip().replace(" ",""))
### 芝ダート障害 ###
## 芝左1600m
## 障芝 外-内2850m 菊花賞なんかも外回り
# 種類が多いので含まれているかでチェック
print("race_cource : " + re.split('/',xml[0].span.string)[0][0])
### どちら回りか？ ###
# 取り出す関数を作ったほうが良いかも
### 距離 ###
# 取り出す関数を作ったほうが良いかも
### 天気 ###
print("race_tenki : " + (re.split('/',xml[0].span.string)[1]).split(':')[1].replace(" ",""))
### 馬場状態 ###
print("race_bb : " + (re.split('/',xml[0].span.string)[2]).split(':')[1].replace(" ",""))


print("---------------")
# print(xml[0].span.string)
# li = re.split('/',xml[0].span.string)
# moji=li[0]
# print(moji)
# print(moji[0])
# moji=moji[1:]
# print(moji)

# for l in li:
#     print(l)

### 会場 ###

### 馬名 ###
### 性 ###
### 馬齢 ###
### 人気 ###
### 倍率 ###
### 父 ###
### 母 ###
### 母父 ###
### 馬体重 ###
### 騎手 ###
### 調教師 ###

# # タグつきで同じものが２つ引っかかる
# races = soup.find_all('a',href=re.compile("^/\?pid=race\&"))
# list_race=[]
# for race in races:
#     list_race.append(base_url + race.get('href'))
#     # print(base_url + race.get('href'))

# # 重複を削除する（※divのclassでFilterできないか？）
# list_uniq = list(set(list_race))
# for url in list_uniq:
#     print(url)


# # お試し
# print("-----------------------")
# # li = soup.select('div[class^="racename"]')
# li = soup.select('div.racename')
# for l in li:
#     print(" - - - -  -")
#     # print(l)
#     a = l.find_all('a',href=re.compile("^/\?pid=race\&"))
#     print(a)
#     print(a[0].get('href'))
#     for b in a:
#         print(b.get('href'))

# print([a.get("href") for a in li.find_all("a")])

html.close()


