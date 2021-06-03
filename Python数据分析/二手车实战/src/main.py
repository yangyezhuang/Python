import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

font = {
    'size': 13,
    'color': 'red'
}

plt.figure(figsize=(12, 8))
plt.subplots_adjust(wspace=0.5, hspace=0.5)


class Graph(object):
    df = pd.read_csv(
        r'E:\Code\PycharmProjects\Projects\二手车实战\data\car.csv', encoding='gbk')

    # 二手车数量排行前十的城市
    def g1(self):
        df1 = self.df['city'].value_counts()[:10]
        labels = df1.index.tolist()
        data = df1.values.tolist()
        plt.subplot(231)
        plt.title('二手车数量排行前十的城市', fontdict=font)
        plt.plot(labels, data, '-o', label='单位(辆)')
        plt.legend()
        plt.ylim(300, 800)

    # 排行前十的品牌
    def g2(self):
        df2 = self.df['title'].value_counts()[:5]
        labels = df2.index.tolist()
        data = df2.values.tolist()
        plt.subplot(232)
        plt.title('排行前十的品牌', fontdict=font)
        plt.plot(labels, data, '--rd', label='单位(辆)')
        plt.legend()
        plt.ylim(200, 2200)

    # 价格排行前五的车型
    def g3(self):
        df1 = self.df.sort_values(by='price', ascending=False)
        df11 = df1.drop_duplicates(['title'])
        df111 = df11[['title', 'price']][:5]
        labels = df111['title'].tolist()
        data = df111['price'].tolist()
        plt.subplot(233)
        plt.title('价格排行前五的车型', fontdict=font)
        plt.bar(labels, data, label='单位(万元)')
        plt.legend()
        plt.ylim(60, 110)

    # 各品牌所占市场份额
    def g4(self):
        df2 = self.df['title'].value_counts()[:5]
        labels = df2.index.tolist()
        data = df2.values.tolist()
        plt.subplot(234)
        plt.title('各品牌所占市场份额', fontdict=font)
        explode = [0]*len(labels)
        plt.pie(data,explode,labels, pctdistance=0.8,autopct='%.2f%%')
        plt.legend(loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=8)


    def g5(self):
        pass

    def g6(self):
        pass


def main():
    g = Graph()
    g.g1()
    g.g2()
    g.g3()
    g.g4()
    # g.g5()
    # g.g6()
    plt.show()


if __name__ == '__main__':
    main()
