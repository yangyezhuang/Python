from graph import line, bar, pie, ring, radar, rose
from func import menu


def graph_menu(subjects, score):
    print('1-打印折线图\n'
          '2-打印柱状图\n'
          '3-打印饼图\n'
          '4-打印环形图\n'
          '5-打印雷达图\n'
          '6-打印玫瑰图\n')

    tools = {'1': line, '2': bar, '3': pie, '4': ring, '5': radar, '6': rose}
    choose = input('Please input：')
    if choose in tools:
        tools[choose](subjects, score)
    elif choose == 'q':
        menu()
    else:
        pass
