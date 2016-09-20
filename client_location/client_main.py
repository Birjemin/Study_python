#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib2
import urllib
import socket


class Client(object):

    URL = "http://int.dpool.sina.com.cn/iplookup/iplookup.php"

    def __init__(self, ip=None):
        if ip is None:
            self.data = {'ip': socket.gethostbyname(socket.gethostname()), 'format': 'js'}
        else:
            self.data = {'ip': ip, 'format': 'js'}

    def get_response_from_url(self):
        decode_data = urllib.urlencode(self.data)
        req = urllib2.Request(self.URL, decode_data)
        try:
            return urllib2.urlopen(req).read().decode('gbk')
        except Exception as e:
            return "urlopen Exception : %s" % e

    def get_location(self):
        return self.get_response_from_url()

if __name__ == '__main__':
    obj_ip = Client('60.191.51.59')
    print obj_ip.get_location()
