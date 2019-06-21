import itchat
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import os

# 首先安装依赖库
# pip install itchat
# pip install jieba
# pip install wordcloud

# 登录微信部分代码，获取个性签名
itchat.auto_login(enableCmdQR=2)
print("开始获取微信好友个性签名....")
friends = itchat.get_friends(update=True)
signature = ''
for friend in friends:
    sign = str(friend['Signature'])
    if len(sign) == 0:
        continue
    # 去除一些样式签名
    signature += sign.replace("<span", "") \
        .replace("class", "") \
        .replace("</span>", "") \
        .replace("emoji", "") \
        .replace(" ", "") \
        .replace("\n", "")

wordList = jieba.cut(signature, cut_all=True)
# 将jieba 分割的字符以空格拼成一整个字符串
text = " ".join(wordList)
print("好友个性签名获取成功")
print(text)

# 获取当前文件的执行路径
src_dir = os.getcwd()
# 生成词云形状的图片地址
imagePath = src_dir + "\\ciyun.png"
# 生成词云字体地址（防止中文乱码）
font = src_dir + "\\SimHei.ttf"
# 生成的词云图地址
resultPath = src_dir + "\\好友个性签名词云图.png"

print("开始生成微信好友个性签名词云...")
# 开始生成图片
bg = np.array(Image.open(imagePath))
wc = WordCloud(
    mask=bg,  # 造型遮盖
    background_color="white",  # 背景颜色
    max_font_size=150,  # 字体最大值
    min_font_size=5,  # 字体最小值
    max_words=5000,  # 词云显示的最大词数
    random_state=40,  # 设置有多少种随机生成状态，即有多少种配色方案
    font_path=font,  # 设置字体
).generate(text)
wc.to_file(resultPath)
print("词云图片已生成" + resultPath)
