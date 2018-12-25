#!/usr/bin/python
'''
from urllib import urlopen

url=r'https://www.baidu.com/'
log=open('logfile.txt','w')
print>>log,('Downloading file from %s') % url
text=urlopen(url).read()
print>>log,('File successfully download')
'''

import logging
logging.basicConfig(level=logging.INFO,filename='logfile.txt')
logging.info('Start program')
logging.info('Trying to divide 2 by 2')
print 2/2
logging.info('The division succeeded')
logging.info('Trying to divide 2 by 0')
print 2/0
logging.info('The division succeeded')
logging.info('Ending program')

