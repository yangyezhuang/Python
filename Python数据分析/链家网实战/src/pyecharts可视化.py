from pyecharts.charts import Bar, Line, Pie, Funnel, Page, Radar
from pyecharts import options as opts
import pandas as pd

# 加载数据
df = pd.read_csv(r'..\data\一线城市.csv')


class Test(object):
    def __init__(self):
        data = round(df.groupby(['city']).mean())
        self.city = list(data.index)  # 获取行索引
        self.total_price_mean = data['total_price'].tolist()  # 平均总价
        self.unit_price_mean = data['unit_price'].tolist()  # 平均单价
        self.unit_price_max = (df['unit_price'].groupby(df['city']).max()).tolist()  # 平均最高单价
        self.unit_price_min = df['unit_price'].groupby(df['city']).min().tolist()  # 平均最低单价

    # 各城市二手房平均总格
    def bar1(self):
        bar1 = (
            Bar()
                .add_xaxis(self.city)
                .add_yaxis('万元', self.total_price_mean)
                .set_colors(['skyblue'])
                .set_global_opts(
                yaxis_opts=opts.AxisOpts(name='价格/万'),
                xaxis_opts=opts.AxisOpts(name='城市'),
                title_opts=opts.TitleOpts(title="房屋平均总价", pos_left='center',
                                          title_textstyle_opts=opts.TextStyleOpts(color='red')),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='center', pos_top='6%')
            )
        )
        return bar1

    # 各城市二手房平均单价
    def bar2(self):
        bar2 = (
            Bar()
                .add_xaxis(self.city)
                .add_yaxis('元', self.unit_price_mean)
                .set_colors(['orange'])
                .set_global_opts(
                yaxis_opts=opts.AxisOpts(name='价格/元'),
                xaxis_opts=opts.AxisOpts(name='城市'),
                title_opts=opts.TitleOpts(title="每平米平均价格", pos_left='center',
                                          title_textstyle_opts=opts.TextStyleOpts(color='red')),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='center', pos_top='6%')
            )
        )
        return bar2

    # 每平米平均价格差
    def line1(self):
        line1 = (
            Line()
                .add_xaxis(self.city)
                .add_yaxis('最高价', self.unit_price_max)
                .add_yaxis('最低价', self.unit_price_min)
                .set_global_opts(
                yaxis_opts=opts.AxisOpts(name='价格/元'),
                xaxis_opts=opts.AxisOpts(name='城市'),
                title_opts=opts.TitleOpts(title="每平米单价价格差", pos_right='center',
                                          title_textstyle_opts=opts.TextStyleOpts(color='red')),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='center', pos_top='6%')
            )
        )
        return line1

    # 户型数量分布
    def pie1(self):
        # layout = df['layout'].value_counts()  # 查看各种户型数量
        layout_lab = ['2室1厅', '3室2厅', '3室1厅', '2室2厅', '1室1厅', '4室2厅', '4室1厅']
        layout_value = []
        for i in layout_lab:
            i = len(df[df['layout'] == i])
            layout_value.append(i)

        pie1 = (
            Pie()
                .add(radius="60%", series_name='',
                     data_pair=[(i, j) for i, j in zip(layout_lab, layout_value)])
                .set_global_opts(
                title_opts=opts.TitleOpts(title="户型分布情况", pos_left='center',
                                          title_textstyle_opts=opts.TextStyleOpts(color='red')),
                legend_opts=opts.LegendOpts(is_show=True, orient='vertical', pos_left='0%', pos_top='10%')
            )
        )
        return pie1

    # 楼层分布情况
    def ring1(self):
        one_ten = len(df[(df['floor'] <= 10) & (df['floor'] > 1)])
        ten_twenty = len(df[(df['floor'] <= 20) & (df['floor'] > 10)])
        twenty_thirty = len(df[(df['floor'] <= 30) & (df['floor'] > 20)])
        thirty_forty = len(df[(df['floor'] <= 40) & (df['floor'] > 30)])
        forty_fifty = len(df[(df['floor'] <= 50) & (df['floor'] > 40)])
        more_fifty = len(df[df['floor'] > 50])

        num = [one_ten, ten_twenty, twenty_thirty, thirty_forty, forty_fifty, more_fifty]
        lab = ['1-10层', '10-20层', '20-30层', '30-40层', '40-50层', '50+']
        ring1 = (
            Pie()
                .add(series_name='', radius=['35%', '60%'],
                     data_pair=[(j, i) for i, j in zip(num, lab)])  # 环图
                .set_global_opts(
                title_opts=opts.TitleOpts(title="楼层分布情况", pos_left='center',
                                          title_textstyle_opts=opts.TextStyleOpts(color='red')),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='center', pos_top='6%')
            )
        )
        return ring1

    # 平米分布
    def funnel1(self):
        one_hundred = len(df[(df['area'] > 0) & (df['area'] <= 60)])
        two_hundred = len(df[(df['area'] > 60) & (df['area'] <= 80)])
        three_hundred = len(df[(df['area'] > 80) & (df['area'] <= 100)])
        four_hundred = len(df[(df['area'] > 100) & (df['area'] <= 150)])
        five_hundred = len(df[(df['area'] > 150) & (df['area'] <= 220)])
        other = len(df[df['area'] > 220])

        lab = ['0-60', '60-80', '80-100', '100-150', '150-220', '220+']
        area = [one_hundred, two_hundred, three_hundred, four_hundred, five_hundred, other]

        funnel1 = (
            Funnel()
                .add("平米分布", [list(z) for z in zip(lab, area)])
                .set_global_opts(title_opts=opts.TitleOpts(title="平米分布情况", pos_left='center',
                                                           title_textstyle_opts=opts.TextStyleOpts(color='red')),
                                 legend_opts=opts.LegendOpts(is_show=True, pos_left='center', pos_top='7%')
                                 ))
        return funnel1

    # 平米分布
    # def radar1(self):
    #     one_hundred = len(df[(df['area'] > 0) & (df['area'] <= 60)])
    #     two_hundred = len(df[(df['area'] > 60) & (df['area'] <= 80)])
    #     three_hundred = len(df[(df['area'] > 80) & (df['area'] <= 100)])
    #     four_hundred = len(df[(df['area'] > 100) & (df['area'] <= 150)])
    #     five_hundred = len(df[(df['area'] > 150) & (df['area'] <= 220)])
    #     other = len(df[df['area'] > 220])
    #
    #     area = [one_hundred, two_hundred, three_hundred, four_hundred, five_hundred, other]
    #
    #     data = [{"value": area, "name": "平米分布："}]
    #     c_schema = [
    #         {"name": "60平米以下", "max": 5000, "min": 0},
    #         {"name": "60-80平米", "max": 5000, "min": 0},
    #         {"name": "80-100平米", "max": 5000, "min": 0},
    #         {"name": "100-150平米", "max": 5000, "min": 0},
    #         {"name": "150-220平米", "max": 5000, "min": 0},
    #         {"name": "220平米以上", "max": 5000, "min": 0},
    #     ]
    #     radar1 = (
    #         Radar()
    #             .set_colors(["#4587E7"])
    #             .add_schema(
    #             schema=c_schema,
    #             shape="circle",
    #             center=["50%", "50%"],
    #             radius="80%",
    #             angleaxis_opts=opts.AngleAxisOpts(
    #                 min_=0,
    #                 max_=360,
    #                 is_clockwise=False,
    #                 interval=5,
    #                 axistick_opts=opts.AxisTickOpts(is_show=False),
    #                 axislabel_opts=opts.LabelOpts(is_show=False),
    #                 axisline_opts=opts.AxisLineOpts(is_show=False),
    #                 splitline_opts=opts.SplitLineOpts(is_show=False),
    #             ),
    #             radiusaxis_opts=opts.RadiusAxisOpts(
    #                 min_=0,
    #                 max_=5000,
    #                 interval=1000,
    #                 splitarea_opts=opts.SplitAreaOpts(
    #                     is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
    #                 ),
    #             ),
    #             polar_opts=opts.PolarOpts(),
    #             splitarea_opt=opts.SplitAreaOpts(is_show=False),
    #             splitline_opt=opts.SplitLineOpts(is_show=False),
    #         )
    #             .add(
    #             series_name="平米分布：",
    #             data=data,
    #             areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
    #             linestyle_opts=opts.LineStyleOpts(width=1),
    #         )
    #     )
    #
    #     return radar1


# 拖动布局
def main():
    t = Test()
    bar1 = t.bar1()
    bar2 = t.bar2()
    line1 = t.line1()
    pie1 = t.pie1()
    ring1 = t.ring1()
    funnel1 = t.funnel1()
    # radar1 = t.radar()

    visual_path = r'..\resources/'
    source_html = visual_path + 'source.html'
    dest_html = visual_path + 'index.html'

    grid = (
        # 创建原始html
        # Page(layout=Page.DraggablePageLayout)
        #     .add(bar1, bar2, line1, pie1, ring1, funnel1)
        #     .render(source_html)

        Page()
            .add(bar1, bar2, line1, pie1, ring1, funnel1)
            # 将原始html进行格式化
            .save_resize_html(source=source_html,
                              cfg_file=visual_path + 'chart_config.json',
                              dest=dest_html
                              )
    )
    return grid


if __name__ == '__main__':
    main()
