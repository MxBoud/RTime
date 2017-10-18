#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil, errno, os

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
       
directory = os.path.dirname(__file__)

print directory
src = os.path.join(directory,'Ressources','tablelist5.16')
print src
dst = os.path.join('C:/','Python27','tcl')
print dst

copyanything(src, dst)

src = os.path.join(directory,'Ressources','tablelist.py')
dst = os.path.join('C:/','Python27','Lib','lib-tk')
#copyanything(src, dst)<
shutil.copy(src, dst)
