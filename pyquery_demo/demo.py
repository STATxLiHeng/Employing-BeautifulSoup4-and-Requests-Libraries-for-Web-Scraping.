import requests
import lxml
from pyquery import PyQuery as pq

url = 'http://localhost/shopxo/'
#
response = requests.get(url)
html_content = response.text
#
# #字符串
doc = pq(html_content)
# print(doc)

# URL初始化
# doc = pq(url)
# print(doc)

# 文件初始化
# doc = pq(filename='shopxo.html')
# print(doc)

# print(doc('#search-input'))
# 查找節點

# print(doc('.goods-list').parent())

# print(doc('.banner-news ul li').add_class('banner-news-title'))
# print(doc('.banner-news ul li a')).attr('href')
# links = doc('.banner-news ul li a')
# for item in links.items():
#     print(item.attr('href'))


# 使用偽類
news_list = doc('.banner-news ul li:nth-child(6)')
news_list = doc('.banner-news ul li:nth-child(2n)')
news_list = doc('.banner-news ul li:gt(0)')
print(news_list)