from func.graph_menu import graph_menu
from conf.settings import BaseConfig
from utils.sql import SQLHelper
from conf.settings import conn


# 添加信息
def add_info():
    id = input('请输入学号：')
    name = input('请输入姓名：')
    chinese = input('请输入语文成绩：')
    math = input('请输入数学成绩：')
    english = input('请输入英语成绩：')
    physical = input('请输入物理成绩：')
    chemical = input('请输入化学成绩：')
    cur = conn.cursor()
    sql = "insert into score (id,name,chinese,math,english,physical,chemical) values (%s,%s,%s,%s,%s,%s,%s)"
    values = (id, name, chinese, math, english, physical, chemical)
    cur.execute(sql, values)
    conn.commit()
    print('录入完成！')


# 删除信息
def del_info():
    name = input('请输入姓名：')
    cur = conn.cursor()
    sql = f"delete from score where name='{name}'"
    cur.execute(sql)
    conn.commit()
    print(f'已删除 {name} 相关信息')


# 修改信息
def change_info():
    name = input('请输入姓名：')
    subject = input('请输入要修改的科目：')
    score = input('请输入新成绩：')

    cur = conn.cursor()
    sql = f"update score set {subject}='{score}' where name = '{name}'"
    cur.execute(sql)
    conn.commit()
    # result = cur.fetchall()
    # print(result)


# 查询信息
def search_info():
    name = input('请输入姓名：')
    result = SQLHelper.fetch_one("select * from score where name= %s ", [name, ])
    print(result)
    subjects = list(result.keys())[2:]  # 将字典中所有的键转换为列表形式，并取后五个
    score = list(result.values())[2:]
    # 可视化菜单
    graph_menu(subjects, score)


# 打印信息
def print_score(self):
    result = SQLHelper.fetch_all('select * from score', [])
    for i in result:
        print(i)


