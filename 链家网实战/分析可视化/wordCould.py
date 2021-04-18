import jieba
import wordcloud


# 对文本进行分词
def cut_word(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    txt = file.read()
    words = jieba.lcut(txt)
    # 对词频进行统计
    count = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            count[word] = count.get(word, 0) + 1
    # 引入停用词
    exclude = ['大', '南北']  # 建立无关词语列表
    for key in list(count.keys()):  # 遍历字典的所有键，即所有word
        if key in exclude:
            del count[key]
    lists = list(count.items())
    lists.sort(key=lambda x: x[1], reverse=True)  # 词频排序
    # 打印前15条词频
    for i in range(20):
        word, number = lists[i]
        print("关键字：{:-<5}频次：{}".format(word, number))
    # 词频写入
    with open(word_path, 'w', encoding='gbk') as f:
        for i in range(20):
            word, number = lists[i]
            f.write('{}\t{}\n'.format(word, number))
        f.close()
        return word_path


# 制作词云
def get_cloud(word_path):
    with open(word_path, 'r', encoding='gbk') as f:
        text = f.read()
    wcloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                                 background_color='white',
                                 width=500,
                                 max_words=1000,
                                 height=400,
                                 margin=2).generate(text)
    wcloud.to_file(pic_path + 'wordCloud.png')  # 指定词云文件路径
    f.close()
    print("词云图片已保存")


file_path = r'E:\Code\PycharmProjects\数据统计分析及软件应用\链家网实战\data\词云.txt'
word_path = r'E:\Code\PycharmProjects\数据统计分析及软件应用\链家网实战\data\result.txt'
pic_path = r'E:\Code\PycharmProjects\数据统计分析及软件应用\链家网实战\visual/'

if __name__ == '__main__':
    cut_word(file_path)
    get_cloud(word_path)
