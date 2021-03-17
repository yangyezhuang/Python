import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
font = {
    'color': 'r',
    'size': 13
}


def pie(subjects, score):
    plt.title('饼图',fontdict=font)
    expolde = [0.01] * len(subjects)
    plt.pie(score, expolde, subjects, pctdistance=0.8, autopct='%.2f%%')
    plt.show()

