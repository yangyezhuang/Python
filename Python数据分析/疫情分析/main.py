import matplotlib.pyplot as plt
import pandas as pd
import time

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False


# 计时功能
def total_time(func):
    def a():
        start = time.time()
        result = func()
        stop = time.time()
        print('end timer:%fs.' % (start - stop))
        return result
    return a


# python装饰器
@total_time
def func():
    df = pd.read_csv('./epidemic.csv')
    lists = []
    citys = df['city'].unique().tolist()  # unique取唯一值
    date = df['date'].unique().tolist()

    for city in citys:
        c = df[df['city'] == city]
        bad_num = c['bad'].tolist()
        lists.append(bad_num)

    # 调用绘图函数
    graph(date, lists, citys)


#  绘图
def graph(date, lists, citys):
    plt.title('2020年各月份确诊趋势', fontsize=20)
    for j in range(len(lists)):
        plt.plot(date, lists[j], label=citys[j])
    plt.legend(loc='lower left', fontsize=9, bbox_to_anchor=[1, 0.5, 0.5, 1])
    plt.ylabel('累计确诊')
    plt.xlabel('日期')
    plt.xticks(rotation=300)
    plt.show()


if __name__ == '__main__':
    func()
