#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lagou_spider import html_outputer
import urllib
import urllib2
import re
import json


class Lagou(object):

    def __init__(self, url, pn):
        self.url = url
        self.data = {'first': 'true', 'kd': 'python', 'pn': str(pn)}
        self.page = {}
        self.html = html_outputer.HtmlOutputer()

    def query(self):
        decode_data = urllib.urlencode(self.data)
        request = urllib2.Request(self.url, decode_data)
        response = urllib2.urlopen(request)
        page_code = response.read().decode('utf-8')
        page_json = json.loads(page_code)
        page_json = page_json['content']['positionResult']
        self.page = page_json['result']

    def regex(self):
        i = 0
        for i in range(len(self.page)):
            self.html.collect_data(self.page[i])
            i = i + 1

    def output(self):
        self.html.output_html()

if __name__ == "__main__":
    root_url = "http://www.lagou.com/jobs/positionAjax.json?"
    obj_spider = Lagou(root_url, 4)
    obj_spider.query() #启动爬虫
    obj_spider.regex()
    obj_spider.output()
