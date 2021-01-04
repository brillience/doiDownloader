# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from uuid import uuid4

# useful for handling different item types with a single interface
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline

class DoiDownloaderPipeline:
    def process_item(self, item, spider):
        return item

class fileDown(FilesPipeline):
    def get_media_requests(self, item, info):
        # 向FilesPipline提交url地址，进行文件下载
        for url in item['file_urls']:
            yield Request(url)

    def file_path(self, request, response=None, info=None):
        file_name = uuid4().hex + '.pdf'
        return file_name
