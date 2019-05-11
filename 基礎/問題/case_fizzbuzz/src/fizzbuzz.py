# coding: UTF-8

def fizzbuzz(num):
    rtn = ""
    if num % 3 == 0:
        rtn += "fizz"
    if num % 5 == 0:
        rtn += "buzz"
    return rtn

