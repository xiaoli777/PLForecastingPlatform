#coding:utf-8
import urllib.request

page = urllib.request.urlopen('https://btc.com/336xGpGweq1wtY4kRTuA4w6d7yDkBU9czU')
htmlcode = page.read()
#print htmlcode

pageFile = open('pageCode.txt','wb+')#以写的方式打开pageCode.txt
pageFile.write(htmlcode)#写入
pageFile.close()#开了记得关