from func.menu import menu
from conf import conn
import pymysql

# 登录


def login():
    username = input('请输入用户名：')
    passwd = input('请输入密码：')

    # 进入数据库查找当前用户的密码
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = f"select passwd from users where username= '{username}'"
    cur.execute(sql)
    result = cur.fetchall()
    pwd = result[0]['passwd']
    # print(pwd)

    if passwd == pwd:
        print(f'\n{username},欢迎回来\n')
        menu()
    else:
        print('账号或密码错误')
