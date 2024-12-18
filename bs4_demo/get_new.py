from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://localhost/shopxo/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content,'lxml')

news = soup.select('.banner-news ul li a')
links = []
# print(news)
for item in news:
    link = item.get('href')
    links.append(link)
print(links)

for link in links[1:]:
    response = requests.get(link)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    title = soup.find('h1',{'class':'am-article-title'})
    print(title)