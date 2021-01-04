#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/4 16:02
# @Author : ZhangXiaobo
# @Software: PyCharm

# from scrapy import cmdline
# cmdline.execute('scrapy crawl doi_down'.split())
# input('Press any key to quit.')
#

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('doi_down')
process.start()
input('Press any key to quit.')