#本程序实现在百度搜索中搜索“灌篮高手”，从返回的页面中提取相关的网址信息并存入txt文件
#author：yangkai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #导入键盘模块
import requests
from requests.exceptions import RequestException
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #特定情况下等待




def search(): #得到最终的url地址
    broswer = webdriver.Chrome() #使用Firefox时由于版本问题报错
    broswer.get("http://www.baidu.com")
    click = broswer.find_element_by_id("kw").click()
    input = broswer.find_element_by_id("kw")
    #input = broswer.find_element_by_id("kw")  #baidu对应的搜索为kw关键字
    input.send_keys(u'灌篮高手') #加u使用Unicode编码方式
    #time.sleep(1)
    #input.clear()
    #input.send.keys('slamdumk')
    #broswer.implicitly_wait(10)  # 等待浏览器10s钟，隐式等待，直接等待10s
    #wait = WebDriverWait(broswer,10)
    #wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    input.send_keys(Keys.ENTER)
    #time.sleep(20)
    url = broswer.current_url #这里若不等待，浏览器还未刷新，得到的url就还是之前的url
    print(url)
    return url

def get_page(url):  #由url转换得到处理对象HTML
    try:
        response = requests.get(url)
        if response.status_code == 200: #返回值为200说明响应成功
            print(response.text) #打印出HTML内容
            return response.text #服务器返回的内容
        return None
    except RequestException:
        return None

def parse(html): #注意处理的是HTML数据
    #pattern = re.compile('<div class=.*?<g-img><img id=.*?src="(.*?)".*?</g-img>.*?</div><!--n-->',re.S)
    pattern = re.compile('<div class.*?data-tools="{(.*?)}".*?</div>', re.S)
    result = re.findall(pattern,html)
    print(result)
    i = 0
    for each in result:
        try:
            #pic = requests.get(each, timeout=10)  #对于每一个url都要请求
            #name = str(i)
            fp = open('C:\\Users\\ds\\Desktop\\down\\result.txt','a')
            fp.write(each+'\n') #将每个结果作为一列存储
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