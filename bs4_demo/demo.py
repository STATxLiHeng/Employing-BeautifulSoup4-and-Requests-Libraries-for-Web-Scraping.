from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://localhost/shopxo'
try:
    response = requests.get(url)
except:
    raise  Exception("請求失敗")

html_content = response.text
# print(html_content)

soup = BeautifulSoup(html_content,'lxml')

# print(soup)
# print(soup.title.string)
# print(soup.a)


# print(soup.em.next_sibling)
# print(soup.em.next_sibling.next_sibling)

# 父節點
# # print(soup.em.parent.parent.parent)
# for item in soup.em.parent:
#     print(item)
#     print('\n')

# find 方法
# nav = soup.find('ul', {'class':'top-nav-right'})
# # print(nav)
# for item in nav.children:


# find_all
nav = soup.find_all('div',{'class':'top-nav-items'})
# print(nav)
# for item in nav:
#     if item.span:
#         print(item.span.string)

# select
nav=soup.select('.top-nav-items  .login-event')
print(nav)
for item in nav:
    if item.text != '\n':
        print(item.text)