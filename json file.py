import json
import string

jsn = '{"address":[{"country":"china","city":"wuhan","street":"huangpi"},\
                  {"country":"japan","city":"tokyo","street":"osaki"}]}'
#读取json数据

with open('data.json','r') as f: #读取json文件
    p_data = json.load(f)

j = open('data.json','r') #注意这种文件打开方式，先open，再read
read_data = j.read()

data = {'name':'yang','age':27,'home':'china'} #python dict数据
j_data = json.dumps(data) #将python的dict数据编码成json数据
py_data = json.loads(j_data) #将json数据编码成python dict数据
p_data1 = json.loads(jsn)
print(j_data) #json
print(py_data) #dict
print(p_data1["address"]) #dict
re = json.loads(read_data) #json->dict
print(re["address"])
print(p_data["address"][1]["country"][2]) #注意字典的访问方式，键值后面只能跟数字



if __name__ == "__main__":
    pass