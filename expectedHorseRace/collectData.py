# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
# url = "http://www.nikkei.com/"
url = "http://race.netkeiba.com/?pid=race&id=c201802020411&mode=shutuba"

html = urllib2.urlopen(url)

soup = BeautifulSoup(html,"html.parser")

table = soup.find_all("table")
print table