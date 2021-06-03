import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

title_style = {
    'size': 16,
    'color': 'red'
}

plt.figure(figsize=(18, 9))
plt.subplots_adjust(wspace=0.5, hspace=0.8)


class Graph(object):
    def __init__(self):
        self.df_data = pd.read_csv('data\car.csv', encoding='gbk')
        self.df = self.df_data.dropna()  # 删除带有缺失值的行

    # 二手价排行前五
    def g1(self):
        df1 = self.df.sort_values(by='price', ascending=False)
        df11 = df1.drop_duplicates()  # 对title列去重
        df111 = df11[['title', 'price']][:10]
        df1_title = df111['title'].tolist()
        df1_price = df111['price'].tolist()

        plt.subplot(231)
        plt.title('二手价排行前八', fontdict=title_style)
        plt.bar(df1_title, df1_price)
        for x, y in enumerate(df1_price):
            plt.text(x-0.4, y+0.5, y)
        plt.ylim(50, 105)
        plt.xticks(rotation=300)

    # 二手车数量前十的城市
    def g2(self):
        df2 = self.df['city'].value_counts()[:10]
        city = df2.index.tolist()
        total = df2.values.tolist()

        plt.subplot(232)
        plt.title('二手车数量前十的城市', fontdict=title_style)
        plt.bar(city, total, color='orange')
        for x, y in enumerate(total):
            plt.text(x-0.4, y+0.5, y)
        plt.ylim(300, 800)

    # 原价排行前十与二手价对比
    def g3(self):
        a = self.df.sort_values(
            'origin_price', ascending=False).drop_duplicates(['title'])
        a1 = a[['title', 'origin_price', 'price']].head(10)
        a1_title = a1['title'].tolist()
        a1_origin = a1['origin_price'].tolist()
        a1_now = a1['price'].tolist()

        plt.subplot(233)
        plt.title('原价与二手价对比', fontdict=title_style)
        plt.plot(a1_title, a1_origin, '-o', label='原价')
        plt.plot(a1_title, a1_now, '-o', label='二手价')
        plt.legend(loc='lower left', bbox_to_anchor=[1, 0.5, 0.5, 1])
        plt.xticks(rotation=300)

    # 市场占有率前五的品牌
    def g4(self):
        df3 = self.df['title'].value_counts()[:5]
        df3_title = df3.index.tolist()
        df3_total = df3.values.tolist()

        plt.subplot(234)
        plt.title('市场占有率前五的品牌', fontdict=title_style)
        explode = [0.01]*len(df3_title)
        plt.pie(df3_total, explode, df3_title,
                pctdistance=0.7, autopct='%.2f%%')
        plt.legend(loc='lower left', fontsize=8,
                   bbox_to_anchor=[1, 0.5, 0.5, 1])

    # 排量对比
    def g5(self):
        pl = self.df['排量'].value_counts()
        pl_title = pl.index.tolist()[:5]
        pl_num = pl.values.tolist()[:5]

        plt.subplot(235, projection='polar')
        plt.title('排量对比(单位：T)', fontdict=title_style)
        theta = np.linspace(0, 2*np.pi, len(pl_title), endpoint=False)
        theta = np.concatenate((theta, [theta[0]]))
        pl_title = np.concatenate((pl_title, [pl_title[0]]))
        pl_num = np.concatenate((pl_num, [pl_num[0]]))
        plt.polar(theta, pl_num)
        for x, y in zip(theta, pl_num):
            plt.text(x, y, y)
        plt.fill(theta, pl_num, alpha=0.4)
        plt.thetagrids(theta*180/np.pi, pl_title)

    # 不同年份二手车数量
    def g6(self):
        time = self.df.drop(
            self.df[self.df['time'] == 3008].index | self.df[self.df['time'] == 4008].index)
        t1 = time['time'].value_counts()
        year = t1.index.tolist()[:10]
        v = t1.values.tolist()[:10]

        plt.subplot(236, projection='polar')
        plt.title('不同年份二手车数量', fontdict=title_style)
        plt.axis(False)
        plt.polar()
        theta = np.linspace(0, 2*np.pi, len(year), endpoint=False)
        plt.bar(theta, v, width=0.7, color=np.random.random((len(year), 3)))
        for i in range(len(year)):
            plt.text(theta[i], v[i], year[i],
                     rotation=theta[i] * 180 / np.pi,  # 文字角度
                     rotation_mode='anchor',  # 标签起始位置不再是左上角
                     size=8)
        plt.axis(False)


def main():
    g = Graph()
    g.g1()
    g.g2()
    g.g3()
    g.g4()
    g.g5()
    g.g6()
    plt.savefig('resources/index.jpg')
    plt.show()


if __name__ == '__main__':
    main()
