import scrapy
from doi_downloader.items import DoiDownloaderItem
from scrapy import Request
import re
import sys
sys.path.append('../../')

class DoiDownSpider(scrapy.Spider):
    name = 'doi_down'

    def start_requests(self):
        dois = []
        with open('dois.txt','r') as f:
            for doi in f.readlines():
                dois.append(doi.strip())
        f.close()
        for doi in dois:
            detail_url = 'https://www.sci-hub.ren/' + doi
            print('开始下载', detail_url)
            yield Request(detail_url, callback=self.parse, meta={'doi': doi})

    def parse(self, response):
        detail_url_list = response.xpath('//*[@id="buttons"]/ul/li[2]/a/@onclick')
        item = DoiDownloaderItem()
        item['file_urls'] = []
        if len(detail_url_list) == 0:
            print('==' * 50)
            print('当前doi下载文献失败：', response.meta['doi'])
            print('==' * 50)

        else:
            # 提取第一个目标Selector的内容
            target = detail_url_list.extract_first()
            find_url = re.compile(r"href='(.*?)'")
            target_url = re.findall(find_url, target)[0]
            if target_url[0] != 'h':
                target_url = 'https:' + target_url
            if "\\" in target_url:
                target_url = target_url.replace('\\', '')
            item['file_urls'].append(target_url)
            yield item
