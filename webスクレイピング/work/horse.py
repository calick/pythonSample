# coding: UTF-8
from enum import Enum, auto
import re

import requests
from bs4 import BeautifulSoup
from time import sleep

def getParent(url):
    # target_url="http://db.netkeiba.com/horse/" + url
    # r = requests.get(target_url)
    # soup = BeautifulSoup(r.text, 'lxml')
    # sleep(0.5)
    print(url)
    return ["父","母","母父"]

class Kind(Enum):
    SHIBA="芝"
    DATO="ダ"
    SYOGAI_S="障芝"
    SYOGAI_SD="障芝 ダート"

class Around(Enum):
    RIGHT="右"
    LEFT="左"
    LINE="直線"

class OUTIN(Enum):
    OUT="外"
    IN_OUT="内-外"
    OUT_IN="外-内"

class Horse:
    # 出走したレースを一意に識別するID
    def set_race_id(self,race_id):
        self.race_id=race_id

    # 出走したレース名
    def set_race_name(self,race_name):
        self.race_name=race_name

    # 出走したレースの開催日
    def set_race_date(self,race_date):
        self.race_date=race_date

    # レース会場（東京/中山/...）
    def set_race_course(self,race_course):
        self.race_course=race_course

    # その日何番目のレースか
    def set_race_number(self,race_number):
        self.race_number=race_number

    # def race_grade #レースのグレード
    ## 1年分の情報を出力して分類を検討する

    # 距離
    ## パターンが大量にあるため正規表現で
    def set_race_distance(self,data):
        pattern=r"\d\d\d\dm"
        self.race_distance=re.search(pattern,data).group()

    # レース種別（芝/ダート/障害）
    def set_race_kind(self,data):
        for k in Kind:
            if k.value in data:
                self.race_kind=k.value

    # 周り（左/右/直線）
    def set_race_around(self,data):
        self.race_around=""
        for a in Around:
            if a.value in data:
                self.race_around=a.value
    
    # 外 - 内 ※外回りか
    def set_race_outin(self,data):
        self.race_outin=""
        for o in OUTIN:
            if o.value in data:
                self.race_outin=o.value
    
    # 天気
    def set_race_weather(self,race_weather):
        self.race_weather=race_weather

    # 馬場状態
    def set_race_ground_state(self,race_ground_state):
        self.race_ground_state=race_ground_state

    # 馬id
    def set_horse_id(self,horse_id):
        self.horse_id=horse_id

    # 馬名
    def set_horse_name(self,horse_name):
        self.horse_name=horse_name
    def get_horse_name(self):
        return self.horse_name

    # 着順
    def set_horse_order_of_arrival(self,order_of_arrival):
        self.horse_order_of_arrival=order_of_arrival

    # 枠番
    def set_horse_wakuban(self,wakuban):
        self.horse_wakuban=wakuban

    # 馬番
    def set_horse_umaban(self,umaban):
        self.horse_umaban=umaban

    # 単勝
    def set_horse_odds(self,odds):
        self.horse_odds=odds

    # 性別
    def set_horse_sex(self,sex):
        self.horse_sex=sex[0]

    # 馬齢
    def set_horse_age(self,age):
        self.horse_age=age[1:]

    # 人気
    def set_horse_popularity(self,horse_popularity):
        self.horse_popularity=horse_popularity

    # 斤量
    def set_horse_basis_weight(self,basis_weight):
        self.horse_basis_weight=basis_weight

    # 父 / 母 / 母父
    def set_horse_parents(self,horse_parents):
        parents = getParent(horse_parents)
        self.horse_father=parents[0]
        self.horse_mother=parents[1]
        self.horse_granfa=parents[2]

    # 騎手ID
    def set_jockey_id(self,jockey_id):
        self.jockey_id=jockey_id

    # 騎手名
    def set_jockey_name(self,jockey_name):
        self.jockey_name=jockey_name

    # タイム
    def set_horse_race_time(self,horse_race_time):
        self.horse_race_time=horse_race_time

    # 上りタイム
    def set_horse_rise_time(self,horse_rise_time):
        self.horse_rise_time=horse_rise_time

    # 上りタイム順位
    def set_horse_rise_time_rank(self,horse_rise_time_rank):
        rank=""
        if horse_rise_time_rank is "r1ml":
            rank=1
        elif  horse_rise_time_rank is "r2ml":
            rank=2
        elif  horse_rise_time_rank is "r3ml":
            rank=3
        self.horse_rise_time_rank=rank

    # 着差
    def set_horse_goal_difference(self,horse_goal_difference):
       self.horse_goal_difference=horse_goal_difference

    # 通過順位
    def set_horse_pass_order(self,horse_pass_order):
        self.horse_pass_order=horse_pass_order

    # 体重
    def set_horse_weight(self,horse_weight):
        self.horse_weight=horse_weight

    # 前回体重差
    def set_horse_weight_difference(self,horse_weight_difference):
        self.horse_weight_difference=horse_weight_difference

    # 調教師
    def set_trainer_id(self,trainer_id):
        self.trainer_id=trainer_id

    # 調教師
    def set_trainer_name(self,trainer_name):
        self.trainer_name=trainer_name

    # オーナーID
    def set_owner_id(self,owner_id):
        self.owner_id=owner_id

    # オーナー
    def set_owner_name(self,owner_name):
        self.owner_name=owner_name

# # 参考
# def setXXX(self,xxx):
#     self.xxx = xxx

    def print(self):
        print(self.race_course)
        print(self.race_id)
        print(self.race_name)
        print(self.race_distance)
        print(self.race_date)
        print(self.race_number)
        print(self.race_weather)
        print(self.race_ground_state)
        print(self.race_kind)
        print(self.race_around)
        print(self.race_outin)
        print(self.horse_order_of_arrival)
        print(self.horse_wakuban)
        print(self.horse_umaban)
        print(self.horse_odds)
        print(self.horse_sex)
        print(self.horse_age)
        print(self.horse_popularity)
        print(self.horse_basis_weight)
        print(self.horse_father)
        print(self.horse_mother)
        print(self.horse_granfa)
        print(self.horse_id)
        print(self.horse_name)
        print(self.jockey_id)
        print(self.jockey_name)
        print(self.horse_race_time)
        print(self.horse_rise_time)
        print(self.horse_rise_time_rank)
        print(self.horse_goal_difference)
        print(self.horse_pass_order)
        print(self.horse_weight)
        print(self.horse_weight_difference)
        print(self.trainer_id)
        print(self.trainer_name)
        print(self.owner_id)
        print(self.owner_name)
        

