import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
font = {
    'color': 'r',
    'size': 13
}


def radar(subjects, score):
    theta = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
    theta = np.concatenate((theta, [theta[0]]))
    subjects = np.concatenate((subjects, [subjects[0]]))
    score = np.concatenate((score, [score[0]]))
    plt.polar(theta, score)
    plt.fill(theta, score, alpha=0.4)
    plt.thetagrids(theta * 180 / np.pi, subjects)
    plt.ylim(0, 100)
    plt.title('雷达图', fontdict=font)
    plt.show()
