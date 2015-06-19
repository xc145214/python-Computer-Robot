#!/usr/bin/env python
# -*- coding: utf-8 -*-

#引入包
import urllib2

#调用方法
response = urllib2.urlopen("http://www.baidu.com")

#输出
print response.read()