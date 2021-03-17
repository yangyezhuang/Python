from func.register import register
from func.login import login


# 退出程序
def quits():
    Q = input("Enter q to quit!")
    if Q.lower() == 'q':
        exit(0)


# 主页
def home():
    print('-' * 20)
    print('欢迎使用学生信息管理系统')
    print('-' * 20)
    print('1 - register\n'
          '2 - login\n'
          'q - quit')
    print('-' * 20)

    tools = {'1': register, '2': login, 'q': quits}

    choose = input('please input：')
    if choose in tools:
        tools[choose]()
    else:
        print('请重新输入')

# home()
