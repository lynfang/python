# -*- coding: UTF-8 -*-
import time
import string
import os
import re

#tongwen_list = []
sp_tongwen_list = []
for  tongwen in range(100,999):
    a = str(tongwen)[::-1]
    if a == str(tongwen):
        template1 = 0
        #print a
        #tongwen_list.append(a)
        for a_num in str(a):
            template1 = template1 + int(a_num)
        count[str(a)] = template1
            
for test in count.keys():
    if count[test] < 15:
        print test