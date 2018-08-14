###正则爬取东方财富网股吧评论
import requests
import re
from bs4 import BeautifulSoup
url = 'http://guba.eastmoney.com/list,002769.html'
res = requests.get(url)  #默认是UTF-8
html = res.text
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
for results in soup:
    results = str(results)
    results = re.findall(r'<span class="l1">\d+</span>.*?title="(.*?)" >.*?<a href=".*?"  data-popper="\d+" data-poptype="1" target="_blank">(.*?)</a><input.*? class="l5">(.*?)</span>', html)
    #results = re.findall(r'<span class="l1">\d+</span>.*?title="(.*?)">.*?data-popper="\d+" data-poptype="1" href="(.*?)" target="_blank">(.*?)</a><input.*? class="l5">(.*?)</span>', html)
    for result in results:
        #print(result)
        print(result[0],result[1],result[2])
