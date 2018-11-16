# coding: UTF-8
import argparse
from bs4 import BeautifulSoup

class store_race_information:

    def store_race(self,file_path):
        print("call store_race")
        print(file_path)
        html = open(file_path,"r")
        soup = BeautifulSoup(html,"html.parser")

        # ココ以降にHTML保存の処理を書く
        print("title : " + soup.title.string)
        url_items = soup.find_all('a')
        print("a = ", url_items)
        html.close()



