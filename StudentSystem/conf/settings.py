import pymysql
import matplotlib.pyplot as plt


class BaseConfig:
    plt.rcParams['font.family'] = 'simhei'
    font = {
        'color': 'r',
        'size': 13
    }


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


config = {
    'BaseConfig': BaseConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='mysql',
    port=3306,
    db='students',
    charset='utf8'
)
