# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: 免费下载VIP音乐
import requests
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 '
}
# url = "https://lw-sycdn.kuwo.cn/0fbdc083eafde684ee8f63531cf3ed61/673ac793/resource/30106/trackmedia/M800003V7OMc0D2QCg.mp3"
url = 'https://lv-sycdn.kuwo.cn/2aa3c3b2d56e87da0fa677e9a4b780be/67d43136/resource/30106/trackmedia/M8000040uYbR1AkIDA.mp3'
response = requests.get(url, headers=header)
content = response.content
with open("热爱105℃的你.mp4","wb") as file:
    file.write(content)
