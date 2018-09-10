#coding: UTF-8 
import csv

#### 読み込み ####
#openで読み込む
csv_file = open('./data/sample_noheader.csv','r')
f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

print csv_file
print f

header = next(f)
print header
for row in f:
    for data in row:
        print data
csv_file.close()

print '----------------------'
print '----------------------'

# with文を使う
with open('./data/sample_header.csv','r') as w:
    reader = csv.reader(w)
    header = next(reader)

    for row in reader:
        for data in row:
            print data


#### 書き込み ####
# openで書き込み
list=[1,2,3,4,1]
array2d=[[1,2],[2,3]]

f = open('data/sample_csv_write_1.csv','w')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(list)
writer.writerows(array2d)

f.close()

# with文を使う
with open('data/sample_csv_write_2.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow(list)     # list（1次元配列）の場合
    writer.writerows(array2d) # 2次元配列も書き込める
