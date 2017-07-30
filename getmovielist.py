import requests
from requests.exceptions import RequestException
import re #对正则表达式的支持
import json
from multiprocessing import Pool


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200: #返回值为200说明响应成功
            return response.text #服务器返回的内容
        return None
    except RequestException:
        return None

def parse_page(html): #处理得到的html对象，抽取出所需要的内容输出
    pattern = re.compile('<li>.*?<em class="">(.*?)</em>.*?src="(.*?)".*?"title">(.*?)</span>'
                         +'.*?<p class="">(.*?)<br>.*?</p>.*?average">(.*?)</span>.*?</li>',re.S) #re.S匹配换行符
    items = re.findall(pattern,html)
    # print(items) #输出的是一个list形式
    for item in items: #将得到的list整理成dict形式
        yield{
            'rank':item[0],
            'picture':item[1],
            'name':item[2],
            #'actor': item[3]
            'actor':item[3].strip()[3:], #输出从第3个字符开始（原来的字符里面有换行符/n）
            'score':item[4]
        }

def write_to_file(contents):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(contents,ensure_ascii=False)+'\n')
        f.close()


def main(offset): #offset作为分页功能
    url = "https://movie.douban.com/top250?start="+str(offset)+"&filter="
    html = get_page(url)
    #print(html)
    for item in parse_page(html):
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    #for i in range(10):
    #    main(i*25)
    pool=Pool()
    pool.map(main,[i*25 for i in range(10)])  #多进程加快速度
