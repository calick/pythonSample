#coding: UTF-8 
import os

# macでもwindowsでも動作させるためにos.path.join関数を使ってファイルパスを組み立てる
current=os.getcwd()
print(current)
file_path=os.path.join(current,"test_file.txt")
print(file_path)

f=open(file_path,"w")
f.write("Hello Python World.")
f.close()

# fileの閉じ忘れを防止するための構文
# 日本語などの非アスキー文字を含む場合はencordingを指定するほうが良い
# Shift-Jisでファイルが書かれている場合encordingにcp932を指定する
with open(file_path,"w",encoding="utf-8") as f:
    f.write("Hello Python World...")

l=[]
with open(file_path,"r",encoding="utf-8") as f:
    l.append(f.read())
print(l)    
