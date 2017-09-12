import requests
from requests.exceptions import RequestException
import re #对正则表达式的支持
import json
from multiprocessing import Pool
import urllib

urls= []

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200: #返回值为200说明响应成功
            return response.text #服务器返回的内容
        return None
    except RequestException:
        return None

def parse_page(html): #处理得到的html对象，抽取出所需要的内容输出
    #pattern = re.compile('<li>.*?src="(.*?)".*?</li>',re.S) #re.S匹配换行符
    #pattern = re.compile('<div id="video_.*?<img src="(.*?)" id=.*?</p></div>', re.S)  # re.S匹配换行符
    pattern = re.compile('<div id="video_.*?<a href=.*?<video src="(.*?)".*?</p></div>', re.S)
    items = re.findall(pattern,html)
    print(items) #输出的是一个list形式
    #for each in items:
    #    picURL = 'http://www.xvideos.com' + each
    #    urls.append(picURL)
    i=0
    for each in items:
            try:
                pic = requests.get(each, timeout = 10)
                #file_name = str(i)+'.jpg'
                file_name = str(i)
                fp = open('C:\\Users\\ds\\Desktop\\pic\\'+file_name, 'wb')
                #fp = open(file_name, 'wb')
                fp.write(pic.content)
                fp.close()
                i += 1
            except:
                pass
    print("下载完成")

#def write_to_file(contents):
#    with open('result1.txt','a',encoding='utf-8') as f:
#        f.write(json.dumps(contents,ensure_ascii=False)+'\n')
#        f.close()


#def main(offset): #offset作为分页功能
def main():
    #url = "https://movie.douban.com/top250?start="+str(offset)+"&filter="
    url = "http://www.videos.com/"
    html = get_page(url)
    #print(html)
    parse_page(html)
    #gethtml = urllib.urlopen(url).read()
    #for item in parse_page(html):
    #    print(item)
    #    write_to_file(item)


if __name__ == "__main__":
    #main(25)
    main()
