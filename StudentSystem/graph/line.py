import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
font = {
    'color': 'r',
    'size': 13
}


def line(subjects, score):
    plt.title('折线图', fontdict=font)
    plt.plot(subjects, score)
    plt.ylim(0, 100)
    plt.ylabel('Subjects')
    plt.xlabel('Class')
    plt.show()

