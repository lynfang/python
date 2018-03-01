# -*- coding: UTF-8 -*-
import time
import string
import os
import re

counter = {}
a = 12345
b = 0
for int_a in str(a):
    b = int(int_a) + b

print b

#counter(a) = b   
#sort[line_zone] = lines
counter[a] = b 