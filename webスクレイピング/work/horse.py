# coding: UTF-8
from enum import Enum, auto

class Kind(Enum):
    SHIBA="芝"
    DATO="ダ"
    SYOGAI="障"

class Around(Enum):
    RIGHT="右"
    LEFT="左"

class Distance(Enum):
    D_1000="1000m"
    D_1200="1200m"
    D_1400="1400m"
    D_1600="1600m"
    D_1800="1800m"
    D_2000="2000m"
    D_2100="2100m"
    D_2400="2400m"
    D_2500="2500m"
    D_3000="3000m"
    D_3200="3200m"    

class Horse:
    # def race_id = "" #出走したレースを一意に識別するID

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

    # def  #距離
    def set_race_distance(self,data):
        for d in Distance:
            if d.value in data:
                self.race_distance=d.value

    # レース種別（芝/ダート/障害）
    def set_race_kind(self,data):
        for k in Kind:
            if k.value in data:
                self.race_kind=k.value

    # 周り（左/右）
    def set_race_around(self,data):
        for a in Around:
            if a.value in data:
                self.race_around=a.value
    
    # 天気
    def set_race_weather(self,race_weather):
        self.race_weather=race_weather

    # 馬場状態
    def set_race_ground_state(self,race_ground_state):
        self.race_ground_state=race_ground_state

    # def horse_id #馬id
    # def horse_name #馬名
    # def horse_wakuban #枠番
    # def horse_umaban #馬番
    # def horse_number #着順
    # def horse_win #単勝
    # def horse_popularity #人気
    # def horse_age #馬齢
    # def horse_sex #性別
    # def horse_basis_weight #斤量
    # def horse_jockey #騎手
    # def horse_time #タイム
    # def horse_difference #着差
    # def horse_pass_order #通過順位
    # def horse_rise_time #上りタイム
    # def horse_weight #体重
    # def horse_weight_difference #前回体重差
    # def horse_handler #調教師

# # 参考
# def setXXX(self,xxx):
#     self.xxx = xxx

    def print(self):
        print(self.race_course)
        print(self.race_name)
        print(self.race_date)
        print(self.race_number)
        print(self.race_weather)
        print(self.race_ground_state)
        print(self.race_kind)
        print(self.race_around)

