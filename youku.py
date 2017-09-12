#2017/08/11
#本程序实现在优酷搜索框中输入特定字符，并从跳转的网页中爬取图片
from selenium.webdriver.common.keys import Keys #导入键盘模块
from selenium import webdriver
import requests
import time
import re

url = "http://www.youku.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def get_url():
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_id("headq").clear()
    input = browser.find_element_by_id("headq")
    input.send_keys(u'灌篮高手')
    input.send_keys(Keys.ENTER)
    browser.switch_to_window(browser.window_handles[1])  #得到跳转页面的信息
    #time.sleep(10)
    url2 = browser.current_url
    print(url2)
    return url2

def get_html(url):
    response = requests.get(url,headers = headers)  #注意加头，伪装成浏览器
    response.encoding = 'utf-8'  #有时需要加上编码信息
    print(response.text)
    return response.text

def parse(html):
    i = 1
    pattern = re.compile('<div class="s_dir">.*?<img src="(.*?)"></div>.*?</div>',re.S)
    items = re.findall(pattern,html)
    print(items)
    for each in items:
        name = str(i) + '.jpg'
        pic = requests.get(each, timeout=1)  #每个图片对应一个url，重新请求
        fp = open("C:\\Users\\ds\\Desktop\\down\\"+name,'wb')
        fp.write(pic.content)
        fp.close()
        print("正在下载第 %s 张" %i)
        i += 1
    print("done!!!")

def main():
    url2 = get_url()
    html = get_html(url2)
    parse(html)

if __name__ == "__main__":
    main()
