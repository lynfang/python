# -*- coding: UTF-8 -*-
import time
import string
import os
import re
import json

from urllib.request import urlopen
from urllib.error import HTTPError




u = urlopen('http://192.168.2.167:8080/api/v1/pods')
resp = json.loads(u.read().decode('utf-8'))



for level_1 in resp['items']:

    if level_1['spec']['containers'][0]['name']  == 'organization':
        print ( level_1['spec']['containers'][0]['name'] + ': \t' + level_1['spec']['containers'][0]['image']  )
        #if 'containers' in level_2.keys():
        
       

