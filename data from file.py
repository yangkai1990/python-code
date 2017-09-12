#_*_coding:utf-8_*_
#read data from file and process

fp = open("C:\\Users\\ds\\Desktop\\population.txt",'r')
row = fp.readlines()
data = []
for item in row:
    list = item.rstrip('\n').split(' ') #split()就是将一个字符串分裂成多个字符串组成的列表
    data.append(list)
print(data)

i = 0
city_list =[]
for a in data:
    city_list.append(a[0])
    i += 1
    print("{}:{}".format(i,city_list[i-1])) #注意format用法，输出格式设定

def display(number):
    print("你选择的是：",city_list[number])
    print("对应的人口情况是：",data[number][1:])

if __name__ == "__main__":
    print(city_list)
    num = int(input("请根据图片输入查询编号："))
    display(num)
