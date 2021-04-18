import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'E:\Code\PycharmProjects\数据统计分析及软件应用\链家网实战\data\一线城市.csv')
# print("数据行数:", len(df))
# print(list(data.index))  # 获取行索引
# print(data['total_price'].tolist())  # 将df列转化为列表

class House(object):
    def __init__(self):
        self.font = {
            'color': 'r',
            'size': 20
        }

    plt.figure(figsize=(30, 20))
    plt.subplots_adjust(wspace=0.7, hspace=0.5)
    plt.rcParams['font.family'] = 'simhei'
    plt.rcParams['axes.unicode_minus'] = False

    # 二手房平均总价
    def bar1(self):
        data = df.groupby(['city']).mean().round(2)
        city = list(data.index)  # 获取行索引
        total_price_mean = data['total_price'].tolist()  # 将df列转化为列表

        plt.subplot(231)
        plt.title('各城市二手房平均价格', fontdict=self.font)
        plt.bar(city, total_price_mean, label='万元')
        for x, y in enumerate(total_price_mean):
            plt.text(x, y, y, ha='center')
        plt.legend()

    # 平均单价
    def bar2(self):
        data = df.groupby(['city']).mean().round(2)
        city = list(data.index)
        unit_price_mean = data['unit_price'].tolist()
        plt.subplot(232)
        plt.title('各城市二手房/平米平均价格', fontdict=self.font)
        plt.bar(city, unit_price_mean, label='元/平米')
        for x, y in enumerate(unit_price_mean):
            plt.text(x, y, y, ha='center')
        plt.legend()

    # 总价最大值与最小值比较
    def line1(self):
        total_price_max = df['total_price'].groupby(df['city']).max()
        city = list(total_price_max.index)
        Max = total_price_max.tolist()
        total_price_min = df['total_price'].groupby(df['city']).min()
        Min = total_price_min.tolist()
        plt.subplot(233)
        plt.title('总价最大值与最小值比较', fontdict=self.font)
        plt.plot(city, Max, 'd-', label='Max/万元')
        for x, y in enumerate(Max):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.plot(city, Min, 'o-', label='Min/万元')
        for x, y in enumerate(Min):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.legend()

    def pie1(self):
        layout_lab = ['2室1厅', '3室2厅', '3室1厅', '2室2厅', '1室1厅', '4室2厅', '4室1厅']
        layout_value = []
        for i in layout_lab:
            i = len(df[df['layout'] == i])
            layout_value.append(i)

        plt.subplot(234)
        plt.title('户型数量分布', fontdict=self.font)
        explode = [0.01] * len(layout_value)
        plt.pie(layout_value, explode, layout_lab, pctdistance=0.8, autopct='%.2f%%')
        plt.legend(loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1])

    def ring(self):
        one_ten = len(df[(df['floor'] <= 10) & (df['floor'] > 1)])
        ten_twenty = len(df[(df['floor'] <= 20) & (df['floor'] > 10)])
        twenty_thirty = len(df[(df['floor'] <= 30) & (df['floor'] > 20)])
        thirty_forty = len(df[(df['floor'] <= 40) & (df['floor'] > 30)])
        forty_fifty = len(df[(df['floor'] <= 50) & (df['floor'] > 40)])
        more_fifty = len(df[df['floor'] > 50])

        num = [one_ten, ten_twenty, twenty_thirty, thirty_forty, forty_fifty, more_fifty]
        lab = ['1-10层', '10-20层', '20-30层', '30-40层', '40-50层', '50+']

        plt.subplot(235)
        plt.title('楼层分布情况', fontdict=self.font)
        explode = [0] * len(num)
        plt.pie(num, explode, lab, pctdistance=0.8, autopct='%.2f%%')
        plt.pie([1], radius=0.4, colors='w')
        plt.legend(loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1])

    def radar(self):
        plt.subplot(236, projection='polar')
        plt.title('平米分布情况', fontdict=self.font)


def main():
    h = House()
    h.bar1()
    h.bar2()
    h.line1()
    h.pie1()
    h.ring()
    h.radar()
    plt.savefig(r'E:\Code\PycharmProjects\数据统计分析及软件应用\链家网实战\visual/matplotlib.png')
    plt.show()


if __name__ == '__main__':
    main()