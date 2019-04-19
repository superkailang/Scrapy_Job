#!/usr/bin/env python
#-*- coding:utf-8 -*-

from scrapy import cmdline
from scrapy.cmdline import execute
import os
import sys
import schedule
import time

#添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名

execute(['scrapy', 'crawl', 'my_spider'])
# execute(['python', '-V'])

def job():
    #print("I'm working...")
    os.system("scrapy crawl my_spider")
    #cmdline.execute('scrapy crawl my_spider'.split(' '))

schedule.every(60).seconds.do(job)
#schedule.every(1).minutes.do(job);
#from subprocess import Popen
#subprocess.Popen("scrapy crawl News")

while True:
    #job();
    schedule.run_pending()
    time.sleep(1)