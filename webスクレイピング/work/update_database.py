# coding: UTF-8
from bs4 import BeautifulSoup
import re
import horse

list_result=[]
file_path="race/201205040911.html"
# file_path="race/201805050403.html"

html = open(file_path,"r")
soup = BeautifulSoup(html,"html.parser")

# 着順一覧を取得
race_table = soup.select('table.race_table_01')
horses = race_table[0].find_all('tr')
# 1行目はいらないので削除
horses.pop(0)

for h in horses:

    race_result = horse.Horse()

    title = re.split('[｜|]',soup.title.string)

    # レースID
    # classがactiveなのは会場と結果払い戻しの部分で１つめに会場が入るのでこの式にした
    race_result.set_race_id(re.split('/',soup.select('a.active')[0].get('href'))[2])

    # レース名
    race_result.set_race_name(title[0])

    # 開催日
    race_result.set_race_date(title[1])

    ### 会場 ###
    # classがactiveなのは会場と結果払い戻しの部分で１つめに会場が入るのでこの式にした
    race_result.set_race_course(soup.select('a.active')[0].string)

    xml = soup.select('dl[class^="racedata fc"]')
    # レース番号
    race_result.set_race_number(xml[0].dt.string.strip().replace(" ",""))

    # レースのグレード

    # 距離
    race_result.set_race_distance(re.split('/',xml[0].span.string)[0])

    # レース種別（芝ダート障害）
    race_result.set_race_kind(re.split('/',xml[0].span.string)[0])

    # 回り(右/左)
    race_result.set_race_around(re.split('/',xml[0].span.string)[0])

    # 回り(外/内)
    race_result.set_race_outin(re.split('/',xml[0].span.string)[0])

    # 天気
    race_result.set_race_weather((re.split('/',xml[0].span.string)[1]).split(':')[1].replace(" ",""))

    # 馬場状態
    race_result.set_race_ground_state((re.split('/',xml[0].span.string)[2]).split(':')[1].replace(" ",""))


    # 馬ID
    race_result.set_horse_id(re.split('/',h.find_all('a',href=re.compile("^/horse"))[0].get('href'))[2])

    # 馬名
    race_result.set_horse_name(h.find_all('a',href=re.compile("^/horse"))[0].string)

    # 着順
    race_result.set_horse_order_of_arrival(h.select('td[class^="txt_r"]')[0].string)

    # 枠番
    race_result.set_horse_wakuban(h.find_all(class_=re.compile("^w"))[0].span.string)

    # 馬番
    race_result.set_horse_umaban(h.select('td[class^="txt_r"]')[1].string)

    # 単勝
    race_result.set_horse_odds(h.select('td[class^="txt_r"]')[3].string)

    # 性
    race_result.set_horse_sex(h.select('td[class^="txt_c"]')[0].string)

    # 馬齢
    race_result.set_horse_age(h.select('td[class^="txt_c"]')[0].string)

    # 人気
    # 上位3番までとそれ以下で指定されるclassが違うためclassでフィルタはしない
    # 開業コードが入っていることがある？★要確認★
    race_result.set_horse_popularity(h.find_all(align="right",nowrap="nowrap")[1].span.string)

    # 斤量
    race_result.set_horse_basis_weight(h.select('td[class^="txt_c"]')[1].string)

    # soup.find_all("a", class_="link", href="/link")
    
    # 血統
    race_result.set_horse_parents(re.split('/',h.find_all('a',href=re.compile("^/horse"))[0].get('href'))[2])
    
    # 馬体重
    race_result.set_horse_weight(re.split('\(',h.select('td[nowrap^="nowrap"]')[14].string)[0])

    # 馬体重(前回体重差)
    race_result.set_horse_weight_difference(re.split('\(',h.select('td[nowrap^="nowrap"]')[14].string)[1][:-1])

    # 騎手ID
    race_result.set_jockey_id(re.split('/',h.find_all('a',href=re.compile("^/jockey"))[0].get('href'))[2])

    # 騎手名
    race_result.set_jockey_name(h.find_all('a',href=re.compile("^/jockey"))[0].string)

    # タイム
    race_result.set_horse_race_time(h.select('td[class^="txt_r"]')[2].string)

    # 上がりタイム
    race_result.set_horse_rise_time(h.select('td[class^="txt_c"]')[3].string)

    # 上がりタイムの順位
    # 1000直など値がない場合も考慮する
    if len(h.select('td[class^="r"]')) is not 0:
        race_result.set_horse_rise_time_rank(h.select('td[class^="r"]')[0].get('class')[0])
    
    # 着差
    race_result.set_horse_goal_difference(h.select('td[nowrap^="nowrap"]')[8].string)
    
    # 通過順位
    race_result.set_horse_pass_order(h.select('td[nowrap^="nowrap"]')[10].string.replace("\n","").replace("\r",""))

    # 調教師ID
    race_result.set_trainer_id(re.split('/',h.find_all('a',href=re.compile("^/trainer"))[0].get('href'))[2])

    # 調教師
    race_result.set_trainer_name(h.find_all('a',href=re.compile("^/trainer"))[0].string)

    # オーナーID
    race_result.set_owner_id(re.split('/',h.find_all('a',href=re.compile("^/owner"))[0].get('href'))[2])

    # オーナー
    race_result.set_owner_name(h.find_all('a',href=re.compile("^/owner"))[0].string)

    list_result.append(race_result)

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
# race_result.print()


for i in list_result:
    print(i.get_horse_name())

html.close()


