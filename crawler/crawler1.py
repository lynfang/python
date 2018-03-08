from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

import requests


def getTitle(url):
    try:
      html = urlopen(url)
    except HTTPError as e:
      return None
    try:
      bsObj = BeautifulSoup(html.read(), "html.parser")
      title = bsObj.body.h1
    except AttributeError as e:
      return None
    return title
title = getTitle("http://192.168.16.243:8090/pages/viewpage.action?pageId=3871236")
if title == None:
  print("Title could not be found")
else:
  #print(title)
  