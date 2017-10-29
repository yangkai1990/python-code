#-*- coding = UTF-8 -*-

#不是绝对相邻的符号之间也可能有空格符需要用.*?匹配，注意；
#可以选取最小的tag进行正则匹配，只要这个tag相对独特
#可先观察得到的html然后选择正则表达式的算法
#（.*？）里面才是目标符号
#不能正确得到html时加上header
#.content是二进制数据（音频），.text是Unicode类型数据（文本）
import requests
import re

URL = 'http://www.budejie.com/video/2'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def get_html():
  response = requests.get(URL,headers=headers)
  html = response.text
  #print(html)
  return html
def parse_func(html):  #注意对应的输入
  pattern = re.compile('<div class=" j-video" id=.*?data-mp4="(.*?)">.*?</div>',re.S)
  items = re.findall(pattern,html)
  return items
def dowload(items):
    n = 1
    for item in items:
      name = str(n)+'.mp4'
      video = requests.get(item).content
      fp=open('C:\\Users\\ds\\Desktop\\python down\\'+name,'wb')
      fp.write(video)
      fp.close()
      print("正在下载第%s个视频"%n)
      n+=1
    print("done!!")

if __name__ == "__main__":
    html = get_html()
    items=parse_func(html)
    dowload(items)







