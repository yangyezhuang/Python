import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
font = {
    'color': 'r',
    'size': 13
}


def rose(subjects, score):
    theta = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
    plt.polar()
    plt.bar(theta, score, width=1.3, bottom=30, color=np.random.random((len(subjects), 3)))
    for i in range(len(subjects)):
        plt.text(theta[i], score[i], score[i])
    plt.axis(False)
    plt.title('玫瑰图', fontdict=font)
    plt.show()
