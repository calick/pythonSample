# coding: UTF-8
import argparse

# create object
parser = argparse.ArgumentParser()

# setteing param
parser.add_argument("--url", help="input URL", type=str)
parser.add_argument("--file", help="a file is url list", type=str)

args = parser.parse_args()

# 参照
print(args.file)
print(args.url)

