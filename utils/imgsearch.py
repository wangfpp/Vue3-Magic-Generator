import os.path
import time

import requests
from scrapy import Selector


def search_img1(img_style):
    while True:
        try:
            res = requests.get("https://www.freepik.com/search", params={
                "format": "search",
                "query": img_style
            }, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
            })
            selector = Selector(response=res)
            return selector.css("figure ::attr(data-image)").extract()
        except Exception as e:
            print(e)
            pass


def search_img(img_style):
    while True:
        try:
            res = requests.get("https://www.pexels.com/zh-cn/search/" + img_style, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Referer": "https://link.zhihu.com/"
            })
            selector = Selector(response=res)
            print(res)
            return selector.css("article img::attr(src)").extract()
        except Exception as e:
            print(e)
            pass


def search_img3(content):
    while True:
        try:
            res = requests.get("https://www.bing.com/images/search?q=" + content, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            })
            selector = Selector(response=res)
            return selector.css(".mimg::attr(src)").extract()
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    g = """法国长棍面包
北欧式可颂面包
德式牛角形面包
瑞典式全麦面包"""
    for e in g.split("\n"):
        with open(os.path.join(r"D:\Backup\Pictures\logo", e.strip() + ".png"), "wb") as f:
            imgs = search_img3(e)
            print(e, imgs)
            img = imgs[0]
            response = requests.get(img)
            f.write(response.content)
        print(f"\public\product\{e.strip()}.png")