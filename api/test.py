'''
Author: shihan
Date: 2023-11-27 14:21:39
version: 1.0
description: 
'''
import requests
from lxml import html


def crawler(word, products_list=[]):
    """ 爬取京东的商品数据 """
    # url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8'.format(word)
    url = 'https://search.jd.com/Search?keyword=bottle&enc=utf-8'


    # 获取HTML文档
    respons = requests.get(url)
    respons.encoding = 'utf-8'
    html_doc = respons.text

    print(html_doc)
    # 打开文件，如果文件不存在则创建，如果文件已存在则覆盖其内容
    with open('test.html', 'w') as file:
        # 写入数据到文件
        file.write(html_doc)

# 文件写入完成后，自动关闭文件，不需要再调用 file.close()

    # 获取xpath对象
    selector = html.fromstring(html_doc)

    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')

    # 解析对应的标题,价格,链接,店铺
    for li in ul_list:

        # 标题
        title = li.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text() | '
                         'div/div[@class="p-name"]/a/@title')
        print(title)
        # 购买链接
        link = li.xpath('div/div[@class="p-name p-name-type-2"]/a/@href | '
                        'div/div[@class="p-name"]/a/@href')

        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text() | '
                         'div/div[@class="p-price"]/strong/i/text()')

        # 店铺
        store = li.xpath('div/div[@class="p-shop"]//a/text() | '
                         'div//a[@class="curr-shop"]/@title')
        print(store)
        products_list.append({
                'title': title[0],
                'price': price[0],
                'link': 'https:' + link[0],
                'store': store[0],
                'referer': '京东'
            })
    

if __name__ == '__main__':
    a = ["bottle"]
    crawler('爬虫', a)
