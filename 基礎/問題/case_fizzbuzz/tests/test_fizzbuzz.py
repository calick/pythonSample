# coding: UTF-8
import pytest
import csv
import os
from src import fizzbuzz

@pytest.mark.parametrize("num,ans", [
    (1, ""),
    (2, ""),
    (3, "fizz"),
    (4, ""),
    (5, "buzz"),
    (6, "fizz"),
    (7, ""),
    (8, ""),
    (9, "fizz"),
    (10, "buzz"),
    (11, ""),
    (12, "fizz"),
    (13, ""),
    (14, ""),
    (15, "fizzbuzz"),
    (16, ""),
    (17, ""),
    (18, "fizz"),
    (19, ""),
    (20, "buzz"),
])
def test_正常系(num,ans):
    assert fizzbuzz.fizzbuzz(num) == ans

# テストデータをファイルから読み込む
test_data=[]
current=os.getcwd()
file_path_header=os.path.join(current,"tests","data.csv")

with open(file_path_header,'r') as w:
    reader = csv.reader(w)
    header = next(reader)
    for row in reader:
        test_data.append([int(row[0]),row[1]])

@pytest.mark.parametrize("num,ans", test_data)
def test_正常系_csv読み込み(num,ans):
    assert fizzbuzz.fizzbuzz(num) == ans

def test_異常系_TypeError():
    with pytest.raises(TypeError):
        fizzbuzz.fizzbuzz("a")


