# coding: UTF-8

def f(x):
    try:
        return float(x)
    except(ValueError):
        print("Invalid value.")

print(f("1"))
print(f(2))
print(f("three"))
