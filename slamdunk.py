#本程序实现在百度搜索中搜索“灌篮高手”，从返回的页面中提取相关的网址信息并存入txt文件
#author：yangkai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #导入键盘模块
import requests
from requests.exceptions import RequestException
import re
import urllib.request

#urllib.request.urlopen(url)

# headers = {'Host': 'search.yahoo.com',
#            'Connection': 'keep-alive',
#            'Cache-Control': 'max-age=0',
#            'Accept': 'text/html, */*; q=0.01',
#            'X-Requested-With': 'XMLHttpRequest',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
#            'DNT': '1',
#            'Referer': 'https://search.yahoo.com/',
#            'Accept-Encoding': 'gzip, deflate, sdch',
#            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
#            }

def search(): #得到最终的url地址
    broswer = webdriver.Chrome() #使用Firefox时由于版本问题报错
    broswer.get("https://www.videos.com/")
    click = broswer.find_element_by_name("q").click()
    input = broswer.find_element_by_name("q")
    #input = broswer.find_element_by_id("kw")
    input.send_keys('julia') #加u使用Unicode编码方式
    input.send_keys(Keys.ENTER)
    url = broswer.current_url #这里若不等待，浏览器还未刷新，得到的url就还是之前的url
    print(url)
    return url

def get_page(url):  #由url转换得到处理对象HTML
    try:
        response = requests.get(url)
        if response.status_code == 200: #返回值为200说明响应成功
            print(response.text) #打印出HTML内容
            response.encoding = 'utf-8'
            return response.text #服务器返回的内容
        return None
    except RequestException:
        return None

def parse(html): #注意处理的是HTML数据
    # pattern = re.compile('<div class.*?<a href="(.*?)".*?>(.*?)&lrm;(.*?)</a>.*?'
    #                      +'<div class="meta abstract">(.*?)</div><div class="meta abstract_2">(.*?)</div>.*?</div>', re.S)
    # pattern = re.compile('div id.*?<a href="(.*?)".*?</a>.*?</div>',re.S)
    pattern = re.compile('div id.*?<a href="(.*?)".*?</a>.*?</div>', re.S)
    result = re.findall(pattern,html)
    print(result)
    i = 0
    for each in result:
        try:
            # pic = requests.get(each, timeout=10)  #对于每一个url都要请求
            name = "http://www.videos.com" + each
            print(name)
            file_name = str(i)+'.mp4'
            pic = requests.get(name, timeout=20)  # 对于每一个url都要请求
            fp = open('C:\\Users\\ds\\Desktop\\down\\result.txt','a')
            fp1 = open('C:\\Users\\ds\\Desktop\\down\\'+ file_name, 'wb') #注意要指定名称
            fp.write(name +'\n') #将每个结果作为一列存储
            fp1.write(pic.content)
            fp1.close()
            fp.close()
            i += 1
        except:
            pass
    print(i)
    print(u"下载完成")

def main():
    url = search()
    html = get_page(url)
    parse(html)

if __name__ == "__main__":
    main()