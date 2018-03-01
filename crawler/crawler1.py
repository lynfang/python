# -*- coding: UTF-8 -*-
import time
import string
import os
import re
import urllib2  


response = urllib2.urlopen("http://www.baidu.com/")  
html = response.read()  
print html 