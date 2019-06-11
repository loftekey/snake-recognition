import requests
from icrawler.builtin import GoogleImageCrawler
from lxml import etree

r = requests.get('https://en.wikipedia.org/wiki/Snakes_of_Australia')
r.encoding = r.apparent_encoding
dom = etree.HTML(r.text)
xpath_a = '//div[@class="mw-parser-output"]/ul/li/a/text()'
items = dom.xpath(xpath_a)
snake_list = set()
i = 0
temp = set()
for item in items:
  i = i+1
  snake_list.add(item)
  temp.add(item.split(" ")[0])
print(snake_list)
print(len(temp))

# snake_list = ("carpetsnake", "grasssnake", "greensnake", "indiacobra", "kingsnake", "nightsnake", "ringsnake", "thundersnake", "vinesnake", "viper", "watersnake")


filters = dict(
  type='photo',
  size='>400x300'
)



for name in snake_list:
  name_list = name.split(" ")
  print(name_list)
  google_crawler = GoogleImageCrawler(
    feeder_threads=2,
    parser_threads=4,
    downloader_threads=8,
    storage={'root_dir': "".join(["./dataset/", name_list[0]])})
  google_crawler.crawl(keyword=name, filters=filters, max_num=500, file_idx_offset=0)