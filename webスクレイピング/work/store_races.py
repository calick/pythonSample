# coding: UTF-8
import store_race_information
import glob
import argparse

# create object
parser = argparse.ArgumentParser()
# setteing param
parser.add_argument("--dir", help="directory of the saved html files.", type=str, default="data")
args = parser.parse_args()

store_race_information_class = store_race_information.store_race_information()
# store_race_information_class = store_race_infomation("test")
li=glob.glob(args.dir + "/*")
for path in li:
    # store_race_information_class.store_race(path)
    print(path)
