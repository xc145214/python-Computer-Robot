#!/usr/bin/env python
# -*- coding: utf-8 -*-

#引入包
import urllib2

url = "http://www.baidu.com"
#构造request
request = urllib2.Request(url)

response = urllib2.urlopen(request)

#输出
print response.read()