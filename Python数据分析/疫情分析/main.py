import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data1.csv')


bj = df[df['city'] == '北京']
date = bj['date'].tolist()
bj_bad = bj['bad'].tolist()

ah = df[df['city'] == '安徽']
ah_bad = ah['bad'].tolist()

gs = df[df['city'] == '甘肃']
gs_bad = gs['bad'].tolist()

fj = df[df['city'] == '福建']
fj_bad = fj['bad'].tolist()

gd = df[df['city'] == '广东']
gd_bad = gd['bad'].tolist()

gx = df[df['city'] == '广西']
gx_bad = gx['bad'].tolist()


plt.title('2020年各月份确诊趋势', fontsize=20)
plt.plot(date, bj_bad, label='北京')
plt.plot(date, ah_bad, label='安徽')
plt.plot(date, gs_bad, label='甘肃')
plt.plot(date, fj_bad, label='福建')
plt.plot(date, gd_bad, label='广东')
plt.plot(date, gx_bad, label='广西')
plt.legend(loc='lower left', fontsize=9, bbox_to_anchor=[1, 0.5, 0.5, 1])
plt.ylabel('累计确诊')
plt.xlabel('日期')
plt.xticks(rotation=300)
plt.show()
