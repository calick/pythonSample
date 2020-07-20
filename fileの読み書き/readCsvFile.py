#coding: UTF-8 
import csv
import os

#### 読み込み ####
#openで読み込む
current=os.getcwd()
file_path_noheader=os.path.join(current,"data","sample_noheader.csv")
file_path_header=os.path.join(current,"data","sample_header.csv")
file_path_csv_write_1=os.path.join(current,"data","sample_csv_write_1.csv")
file_path_csv_write_2=os.path.join(current,"data","sample_csv_write_2.csv")

csv_file = open(file_path_noheader,'r')
f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

print(csv_file)
print(f)

header = next(f)
print( header)
for row in f:
    for data in row:
        print(data)
csv_file.close()

print('----------------------')

# with文を使う
with open(file_path_header,'r') as w:
    reader = csv.reader(w)
    header = next(reader)

    for row in reader:
        for data in row:
            print(data)


#### 書き込み ####
# openで書き込み
list=[1,2,3,4,1]
array2d=[[1,2],[2,3]]

f = open(file_path_csv_write_1,'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(list)
writer.writerows(array2d)

f.close()

# with文を使う
with open(file_path_csv_write_1, 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow(list)     # list（1次元配列）の場合
    writer.writerows(array2d) # 2次元配列も書き込める
