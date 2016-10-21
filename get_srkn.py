#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os

path = u'/Users/restereo/Библиотека Calibre'

_res = 'all_srkn.txt'

g = open(_res, 'w+')

for filename in glob.glob(os.path.join(path, '*/*/*.txt')):

  f = open(filename, 'r')

  for line in f:
    g.write(line)
