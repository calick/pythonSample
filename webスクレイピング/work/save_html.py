# coding: UTF-8
import requests
import os
from io import open

class save_html:

    def save(self,url,name):
        print(url)
        res=requests.get(url)
        res.encoding = res.apparent_encoding

        directory_name = "data"
        if not os.path.isdir(directory_name):
            os.makedirs(directory_name)

        file_name = directory_name + "/" + name + ".html"
        print(res.encoding)
        with open(file_name,'w', encoding=res.encoding) as file:
            file.write(res.text)
            file.close()
