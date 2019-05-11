# coding: UTF-8
import pytest
from src import dice

# 基本的にrandam関数を使っているだけでrandam関数のテストをしたいわけではない

def test_default値の動作を確認():
    default_value = 6
    assert dice.dice() in range(1,default_value+1)

def test_面数指定の動作を確認():
    men = 10
    assert dice.dice(men) in range(1,men+1)

def test_文字列が入力されたときの動作を確認():
    with pytest.raises(TypeError):
        dice.dice("a")
