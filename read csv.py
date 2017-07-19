import csv
with open('E:\python code\data.csv', 'r') as f: #'rb'以二进制读模形式打开
    reader = csv.DictReader(f)
    for row in reader:
        print(row)