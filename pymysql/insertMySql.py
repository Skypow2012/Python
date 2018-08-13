from urllib import request
from bs4 import BeautifulSoup as bs
import pymysql.cursors


# 文章对象
class jjArticle(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def to_string(self):
        return "文章标题：" + self.title + "\n" + "文章链接：" + self.url


# 首页地址
jjUrl = "https://juejin.im/welcome/android"
# 详情地址
jjDetails = "https://juejin.im"

user_agent = "User-Agent"
user_agent_value = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"

resp = request.Request(jjUrl)
# 模拟浏览器
resp.add_header(user_agent, user_agent_value)
resp = request.urlopen(resp)
# 网页返回的数据
htmlCode = resp.read().decode("utf-8")
# 格式化html
soup = bs(htmlCode, "html.parser")
# print(soup.prettify())

# 分析html 得 获取a标签内class属性为title的元素 即为文章的标题
articleList = soup.findAll("a", {"class", "title"})
# 获取到的所有文章标题
allArticle = []
for article in articleList:
    url = article.get("href")
    # 创建一个保存文章的对象
    article = jjArticle(article.string, jjDetails + url)
    allArticle.append(article)

# 将数据插入至MySQL数据库
host = "localhost"
port = 62503
user = "root"
password = "123456"
db = "azhon_py"

for article in allArticle:
    # 连接数据库 port默认为3306
    connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db,
                                 charset="utf8mb4")
    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 创建sql语句
            sql = "insert into `article`(`title`,`url`) values (%s,%s)"
            # 执行sql语句
            cursor.execute(sql, (article.title, article.url))
            # 提交
            connection.commit()
    finally:
        connection.close()
