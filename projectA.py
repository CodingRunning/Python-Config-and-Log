#!/usr/bin/python
#coding=utf-8

from ConfigParser import ConfigParser

CONFIGFILE="project1.cfg"

config=ConfigParser()
#读取配置文件：
config.read(CONFIGFILE)

#打印初始的问候语：
#要查看的区段是'messages'
print config.get('messages','greeting')

#使用配置文件中的一个问题读取半径：
radius=input(config.get('messages','question')+' ')

#打印配置文件中的结果信息：
#以逗号结束，以在同一行显示：
print config.get('messages','result_message'),

#getfloat()将config值转换为float类型：
print config.getfloat('numbers','pi')+radius**2
