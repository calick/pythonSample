# coding: UTF-8
from bs4 import BeautifulSoup
import re

file_path="data/sample.html"
base_url="http://www.netkeiba.com/"

html = open(file_path,"r")
soup = BeautifulSoup(html,"html.parser")

# タグつきで同じものが２つ引っかかる
races = soup.find_all('a',href=re.compile("^/\?pid=race\&"))
list_race=[]
for race in races:
    list_race.append(base_url + race.get('href'))
    # print(base_url + race.get('href'))

# 重複を削除する（※divのclassでFilterできないか？）
list_uniq = list(set(list_race))
for url in list_uniq:
    print(url)


# お試し
print("-----------------------")
# li = soup.select('div[class^="racename"]')
li = soup.select('div.racename')
for l in li:
    print(" - - - -  -")
    # print(l)
    a = l.find_all('a',href=re.compile("^/\?pid=race\&"))
    print(a)
    print(a[0].get('href'))
    for b in a:
        print(b.get('href'))

# print([a.get("href") for a in li.find_all("a")])

html.close()


