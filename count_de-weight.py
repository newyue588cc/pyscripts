#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Script:count.py
Author:mark
Email:LYJ_216@126.com
Desc:de-weight file line
'''

ifd=open("count.log","r+")
h = 0
j = 0

for line in ifd.readlines():
        if not line:
                break
        else:
                h += 1
                with open("output.log","r+") as ofd:
                        if line not in ofd.readlines():
                                ofd.write(line)
                                j += 1
ifd.close()
print "Input file line count: %s" % h
print "Output file line count: %s" % j