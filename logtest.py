#!/usr/bin/python

from urllib import urlopen

url=r'https://www.baidu.com/'

log=open('logfile.txt','w')
print>>log,('Downloading file from %s') % url
text=urlopen(url).read()
print>>log,('File successfully download')


