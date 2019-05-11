## test_sample.pyを実行する
# pytest test_sample.py
## テスト対象を選択しないとカレントディレクトリ配下すべてがテスト対象となる。test_xxxと言う名前のファイル全て
# pytest
## 以下呼び出しで、テストケースごとにPASSED/FAILED/SKIPPEDが表示される
# pytest -v
## 前回FAILEDだったテストだけ再実行　※前回FAILEDがなければ再度全実行される
# pytest -v --lf
## 前回FAILEDだったテストから実行
# pytest -v --ff
## テスト時間を記録
# pytest -v --duration=0
## カバレッジを出力
# pytest -v --cov=.
## カバレッジを出力(網羅できなかったコード行を出力)
# pytest -v --cov=CODE_DIRECTORY --cov-report=term-missing
## カバレッジを出力(網羅できなかったコード行を出力) + 結果をhtml出力
# pytest -v --cov=CODE_DIRECTORY --cov-report=term-missing --cov-report=html
## 特定のテストだけを実行 
# pytest -m [テストケース名:ex. testcase1] -v

import pytest
import time

# fromでディレクトリを指定し、importでファイルを指定する
# __init__.pyの配置が必要
from src import calc

# いろんなテストがあって、テストごとにオブジェクトを作るのではなく、最初に一度だけ作ってテスト間で使い回したい
# 全部のテストが終わったら後始末したい
# → fixtureを使う

# scopeで指定できるのは次の４つ　※session > module > class > function
# session:テスト全体の前後処理
# function:各テストfunction毎に行う前後処理
# class:各テストclass毎に行う前後処理
# module:各テストモジュール毎に行う前後処理
# package:各テストパッケージ毎に行う前後処理
@pytest.fixture(scope="module", autouse=True)
def num():
    a=1
    print("前処理")
    # yieldを書かないと全て前処理となる
    yield a
    print("後処理")

@pytest.fixture(scope="module", autouse=True)
def string():
    a="aaaaa"
    print("前処理")
    yield a
    print("後処理")

@pytest.mark.testcase1
def test_num(num):
    time.sleep(1)
    assert num == 1

@pytest.mark.testcase2
def test_string(string):
    assert string == "aaaaa"

def test_exception_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

# testをSkipしたいとき
@pytest.mark.skip
def test_skip():
    assert 1 == 2

# 複数のパターンのパラメータをテストする場合
# 失敗した数だけfailedに加算される。4パターン全て失敗すれば 4 failed,
@pytest.mark.testcase2
@pytest.mark.parametrize("x,y,sum", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9),
])
def test_add(x, y, sum):
    assert (x + y) == sum

@pytest.mark.testcase1
def test_calc():
    assert calc.add(1,1) == 2
    assert calc.sub(2,1) == 1
    assert calc.multiplication(10) == 100
    assert calc.power(2,5) == 32


