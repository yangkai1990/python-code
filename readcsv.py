import csv
import pytest
import compute #导入module或者其他函数
#with open('E:\python code\data.csv', 'r') as f: #'rb'以二进制读模形式打开
#    reader = csv.DictReader(f)
reader = csv.DictReader(open('E:\python code\dat.csv', 'r'))
a = []  #必须在这里定义，不然最后打印没定义
b = []
def func():
     for row in reader:
        #print(row['visit_datetime'],row['type'],row['brand_id'],row['user_id'])
        #print(row.get('type'))
        #id = row.get('brand_id')
        a.append(row['brand_id']) #row对应是每一行的一个字典
        b.append(row['type'])


