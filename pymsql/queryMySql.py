import pymysql.cursors

# 查询MySQL数据库
host = "localhost"
port = 62503
user = "root"
password = "123456"
db = "azhon_py"

connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db,
                             charset="utf8mb4")
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql = "select `id`,`title`,`url` from `article`"
        # 执行查询sql语句 返回查询到的数量
        count = cursor.execute(sql)
        # print(count)
        # 查询所有数据 返回一个list
        fetchall = cursor.fetchall()
        for result in fetchall:
            # 格式化输出好看那么一点
            print("%d\t--\t%s\n\t\t%s" % (result[0], result[1], result[2]))

        # 查询指定条数数据
        # fetchmany = cursor.fetchmany(size=3)
        # print(fetchmany)
finally:
    connection.close()
