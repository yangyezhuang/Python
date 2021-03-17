import matplotlib.pyplot as plt
from conf.settings import BaseConfig

# plt.rcParams['font.family'] = 'simhei'
# font = BaseConfig.font

subjects = ['a', 'b', 'c']
score = [23, 45, 78]


def ring(subjecs, score):
    plt.title('环形图', fontdict=BaseConfig.font)
    explode = [0] * len(subjecs)
    plt.pie(score, explode, subjecs, pctdistance=0.8, autopct='%.2f%%')
    plt.pie([1], radius=0.4, colors='w')
    plt.show()

