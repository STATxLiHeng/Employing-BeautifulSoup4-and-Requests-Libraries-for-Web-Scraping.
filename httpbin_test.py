import requests
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)
user_agent = ua.random

# url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# headers = {
#  "user-agent": user_agent
# }
# response = requests.get(url,headers = headers)
# print(response)
# print(response.status_code)
# print(response.headers)
# # print(f'content:{response.content}') # Byte
# print(f'content:{response.text}') # 文本
#

url = 'https://e7.pngegg.com/pngimages/218/394/png-clipart-dead-by-daylight-dead-by-daylight-video-game-t-shirt-payday-2-day-light-game-text-thumbnail.png'
headers = {
 "user-agent": user_agent
}
try:
    response = requests.get(url,headers = headers)
except:
    print("失敗")
else:
    print(response.content)
    with open('pic.png','wb') as f:
        f.write(response.content)