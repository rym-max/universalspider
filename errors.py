#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   errors.py
@Time    :   2019/07/01 22:11:22
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

# here put the import lib
class PathNotFoundException(Exception):
    def __init__(self,path):
        print("<<<<<[PathNotFoundException]: [" + str(path) +"] not found")
        