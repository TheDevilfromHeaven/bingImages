import re

import datetime

from pip._vendor import requests

url = 'https://www.bing.com/'
html = requests.get(url).text#获取这个网页源码
Nurl = re.findall('id="bgLink" rel="preload" href="(.*?)&amp;',html,re.S)#正则表达式写好
for temp in Nurl:#循环获取里边的图片，其实这里只有一个
     url = 'https://www.bing.com' + temp
     print(url)
     pic = requests.get(url)#接着把图片保存下来，再提前准备一个bingImage目录用来存放
     file = 'bingImage\\' + str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day) + '.jpg'
     #print(file)
     fp = open(file,'wb')
     fp.write(pic.content)
     fp.close()