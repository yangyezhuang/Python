import os
import csv
import asyncio
import aiohttp
from lxml import etree
from os.path import dirname, abspath

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
                                community = html.xpath('//div[@class="aroundInfo"]/div[1]/a[1]/text()')[0]
                                location = html.xpath('//div[@class="aroundInfo"]/div[2]/span[2]/a[1]/text()')[0]
                                total_price = html.xpath('/html/body/div[5]/div[2]/div[3]/span[1]/text()')[0]
                                unit_price = html.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/text()')[0]
                                area = html.xpath('//div[@class="houseInfo"]/div[3]/div[1]/text()')[0].strip('平米')
                                layout = html.xpath('//div[@class="houseInfo"]/div[1]/div[1]/text()')[0]
                                floor = html.xpath('//div[@class="houseInfo"]/div[1]/div[2]/text()')[0]
                                house_type = html.xpath('//div[@class="houseInfo"]/div[2]/div[2]/text()')[0]
                                release_time = html.xpath('//div[@class="content"]//li[1]/span[2]/text()')[0]
                                title = html.xpath('//div[@class="content"]/div[1]/h1/text()')[0].strip().strip('。')

                                save(city, community, location, total_price, unit_price, layout, area, floor,
                                     house_type, release_time, title)


# 保存为csv
def save(*args):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + '苏州二手房.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([*args])


# 构造url
async def main():
    url_list = []
    for i in range(1, 101):
        url = f'https://su.lianjia.com/ershoufang/pg{i}/'
        url_list.append(url)
    tasks = [asyncio.create_task(parse(url)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
