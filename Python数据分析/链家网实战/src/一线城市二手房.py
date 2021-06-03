from os.path import dirname, abspath
from lxml import etree
import asyncio
import aiohttp
import os
import re
import csv

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
path = dirname(abspath(__file__)) + '/data/'



# 解析数据
async def parse(url):
    async with aiohttp.ClientSession()as session:
        async with session.get(url, verify_ssl=False, headers=headers)as response:
            if response.status == 200:
                response = await response.text()
                html = etree.HTML(response)
                li_lists = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/@href')
                for url in li_lists:
                    async with aiohttp.ClientSession()as session:
                        async with session.get(url, verify_ssl=False, headers=headers)as response:
                            if response.status == 200:
                                response = await response.text()
                                html = etree.HTML(response)
                                city = html.xpath('//div[@class="fl l-txt"]/a[1]/text()')[0].strip('房产网')
                                location = html.xpath('//div[@class="aroundInfo"]/div[2]/span[2]/a[1]/text()')[0]
                                total_price = html.xpath('/html/body/div[5]/div[2]/div[3]/span[1]/text()')[0]
                                unit_price = html.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/text()')[0]
                                area = html.xpath('//div[@class="houseInfo"]/div[3]/div[1]/text()')[0].strip('平米')
                                layout = html.xpath('//div[@class="houseInfo"]/div[1]/div[1]/text()')[0]
                                floor_str = html.xpath('//div[@class="houseInfo"]/div[1]/div[2]/text()')[0]
                                floor = re.sub("\D", "", floor_str)
                                release_time = html.xpath('//div[@class="content"]//li[1]/span[2]/text()')[0]
                                title = html.xpath('//div[@class="content"]/div[1]/h1/text()')[0].strip().strip('。')

                                save(city, location, total_price, unit_price, layout, area, floor, release_time, title)
                                save_cloud_txt(title)


# 保存为csv
def save(*args):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + '一线城市.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(['city','community','location','total_price','unit_price','layout,area','floor','type','time','title'])
        writer.writerow([*args])


# 写入词云文本文件
def save_cloud_txt(title):
    with open(path + '词云文件.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title])


# 构造url
async def main():
    city_urls = ['https://su.lianjia.com/', 'https://bj.lianjia.com/', 'https://sh.lianjia.com/',
                 'https://nj.lianjia.com/', 'https://cd.lianjia.com/']
    url_list = []
    for city in city_urls:
        for i in range(1, 101):
            url = city + f'ershoufang/pg{i}/'
            url_list.append(url)
    tasks = [asyncio.create_task(parse(url)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
