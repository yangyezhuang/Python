import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
font = {
    'color': 'r',
    'size': 13
}


def bar(subjects, score):
    plt.title('柱状图', fontdict=font)
    plt.bar(subjects, score)
    plt.ylim(0, 100)
    plt.xlabel('Subjects')
    plt.ylabel('Score')
    plt.show()
