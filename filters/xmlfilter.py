#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xmlfilter.py
@Time    :   2019/09/01 22:00:24
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

# here put the import lib
import xml.dom.minidom as minidom

doc = minidom.Document()

rootDoc = doc.createElement("doc")
doc.appendChild(rootDoc)

one = doc.createElement('field')
one.setAttribute("name","dc.url")
rootDoc.appendChild(one)

one = doc.createElement("field")
one_text = doc.createTextNode("<>?")
one.appendChild(one_text)
rootDoc.appendChild(one)

print(doc.toprettyxml())