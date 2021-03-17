# from conf.settings import BaseConfig
from func.add_info import add_info, del_info, change_info, search_info


# 菜单
def menu():
    print('1-录入信息\n'
          '2-删除信息\n'
          '3-修改信息\n'
          '4-查询信息\n'
          '5-打印信息\n')

    tools = {'1': add_info, '2': del_info, '3': change_info, '4': search_info}
    choose = input('Please input：')
    if choose in tools:
        tools[choose]()


# menu()
