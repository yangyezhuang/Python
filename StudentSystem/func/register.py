from conf.settings import conn
from func.login import login
import time


# def repeat_input(args):
#     passwd = input('请输入密码：')
#     passwd2 = input('请再次输入密码：')
#     if passwd2 == passwd:
#         write(username, passwd2)
#     else:
#         print('两次密码不一致')
#         register()


# @repeat_input
def register():
    username = input('请输入用户名：')
    passwd = input('请输入密码：')
    passwd2 = input('请再次输入密码：')
    print(passwd2)
    if passwd2 == passwd:
        write(username, passwd2)
    else:
        print('两次密码不一致')
        register()


def write(username, passwd2):
    cur = conn.cursor()
    sql = "insert into users (username,passwd) values (%s,%s)"
    values = (username, passwd2)
    cur.execute(sql, values)
    conn.commit()
    print('-' * 20)
    print('注册成功，请登录')
    print('注册成功，3s后转跳登录界面\n')
    time.sleep(2)
    print('-' * 20)
    login()

# register()
