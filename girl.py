# 爬取校花图片

from urllib import request
from bs4 import BeautifulSoup as bs
import os

dir = "C:\\Users\\Administrator\\Desktop\\xiaohua"
url = "http://www.xiaohuar.com/2014.html"
imgStart = "http://www.xiaohuar.com/"

resp = request.Request(url=url)
resp = request.urlopen(resp)
# 网页返回的数据
htmlCode = resp.read().decode("gbk")

soup = bs(htmlCode, "html.parser")
allGirl = soup.find_all("div", class_="img")
# 创建文件夹
exists = os.path.exists(dir)
if not exists:
    os.makedirs(dir)

for girl in allGirl:
    content = girl.find_all("img")[0]
    name = content.get("alt")
    imgUrl = content.get("src")
    # 判断是不是已http开头的图片地址，不是的话拼接全路径
    if not imgUrl.startswith('http://'):
        imgUrl = imgStart + imgUrl
    # 下载图片
    img = request.Request(imgUrl)
    response = request.urlopen(img)
    with open(r'%s\%s.jpg' % (dir, name), 'wb') as f:
        f.write(response.read())
        print("%s====下载完成..." % name)
