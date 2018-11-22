# coding: UTF-8
from bs4 import BeautifulSoup
import re
import horse
import copy

list_result=[]
file_path="race/201205040911.html"
# file_path="race/201805050403.html"

html = open(file_path,"r")
soup = BeautifulSoup(html,"html.parser")

race_result = horse.Horse()

title = re.split('[｜|]',soup.title.string)
# レース名
race_result.set_race_name(title[0])
# 開催日
race_result.set_race_date(title[1])

xml = soup.select('dl[class^="racedata fc"]')
# レース番号
race_result.set_race_number(xml[0].dt.string.strip().replace(" ",""))

### 芝ダート障害 ###
## 芝左1600m
## 障芝 外-内2850m 菊花賞なんかも外回り
# 種類が多いのでパターンを洗い出す必要がある
race_result.set_race_kind(re.split('/',xml[0].span.string)[0])

print(re.split('/',xml[0].span.string)[0])
print("race_cource : " + re.split('/',xml[0].span.string)[0][0])

# 距離
race_result.set_race_distance(re.split('/',xml[0].span.string)[0])

# 回り(右/左)
race_result.set_race_around(re.split('/',xml[0].span.string)[0])

# 回り(外/内)
race_result.set_race_outin(re.split('/',xml[0].span.string)[0])

# 天気
race_result.set_race_weather((re.split('/',xml[0].span.string)[1]).split(':')[1].replace(" ",""))

# 馬場状態
race_result.set_race_ground_state((re.split('/',xml[0].span.string)[2]).split(':')[1].replace(" ",""))

### 会場 ###
# classがactiveなのは会場と結果払い戻しの部分で１つめに会場が入るのでこの式にした
race_result.set_race_course(soup.select('a.active')[0].string)

race_table = soup.select('table.race_table_01')
horses = race_table[0].find_all('tr')
# 1行目はいらないので削除
horses.pop(0)

# result = copy.deepcopy(race_result)

for horse in horses:
    # result = copy.deepcopy(race_result)
    race_result.set_horse_name(horse.find_all('a',href=re.compile("^/horse"))[0].string)
    # a=horse.find_all('a',href=re.compile("^/horse"))
    # print(a[0].string)
    # races = soup.find_all('a',href=re.compile("^/\?pid=race\&"))
    list_result.append(race_result)


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

# # お試し
# print("-----------------------")

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
print("---------------")
race_result.print()

# for i in list_result:
#     print(i.get_horse_name())

html.close()


