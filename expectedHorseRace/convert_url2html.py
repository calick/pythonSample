# coding: UTF-8
import save_html
import argparse

# create object
parser = argparse.ArgumentParser()
# setteing param
parser.add_argument("--file", help="input URL file path", type=str, default="url_list.txt")

args = parser.parse_args()

save_html_class = save_html.save_html()
with open(args.file,'r') as f:
    for line in f:
        line = line.rstrip('\n')
        str_list = line.split("/")

        # 取得したURLの最後が/で終わっている場合を考慮する
        if(str_list[-1] == ""):
            name = str_list[-2]
        else:
            name = str_list[-1]

        save_html_class.save(line,name)
