import requests
from scrapy import Selector


def search_img(img_style):
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


if __name__ == '__main__':
    search_img("风景")
