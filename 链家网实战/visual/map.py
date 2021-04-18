from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType

city=['北京','上海','南京','苏州','成都']
values=[123,2342,456,35,13]
c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "城市",
        [list(z) for z in zip(city,values)],
        type_=ChartType.EFFECT_SCATTER,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="直观分布",pos_left='center'))
    .render("geo_effectscatter.html")
)
