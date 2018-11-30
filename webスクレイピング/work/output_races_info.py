# coding: UTF-8
from bs4 import BeautifulSoup
import re
import os
from io import open
import glob

os.chdir("race")
file_list = glob.glob("./*")

for file in file_list:
    print(file)
    html = open(file,"r")
    soup = BeautifulSoup(html,"html.parser")

    with open("../races.csv",'a') as file:
        title = re.split('[｜|]',soup.title.string)
        file.write(title[0])
        file.write(",")
        file.write(title[1])
        file.write(",")
        
        xml = soup.select('dl[class^="racedata fc"]')
        file.write((re.split('/',xml[0].span.string)[0]).replace('\xa0',''))
        file.write(",")
        file.write((re.split('/',xml[0].span.string)[1]).split(':')[1].replace('\xa0',''))
        file.write(",")
        file.write(soup.select('a.active')[0].string)
        file.write("\n")
        file.close()

    html.close()


