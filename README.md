###爬取新浪网新闻标题日期网址
import requests
from bs4 import BeautifulSoup
url ='http://news.sina.com.cn/china/' 
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.img-news-item'):
        time=news.select('.time')[0].text
        h2=news.select('h2')[0].text,
        a=news.select('a')[0]['href']
        print(time)
        print(h2)
        print(a)
