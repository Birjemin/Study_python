#coding:utf8
'''
Created on 2016年7月13日

@author: hang
'''


import urllib2


class HtmlDownloader(object):

     def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.code != 200:
            return None

        return response.read()


