import requests

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
response = requests.get(url)
data = response.json()
print(data['Data']['Count'])


def get_url(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None