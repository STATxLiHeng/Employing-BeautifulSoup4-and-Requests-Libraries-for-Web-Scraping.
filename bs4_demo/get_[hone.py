from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://localhost/shopxo/?s=search/index/wd/6E98B86EC9AB.html'
try:
    response = requests.get(url)
except:
    raise  Exception("請求失敗")

html_content = response.text
print(html_content)
soup = BeautifulSoup(html_content,'lxml')