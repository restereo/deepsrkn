#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os

path = u'/Users/restereo/Библиотека Calibre/Fiedor Mikhailovich Dostoievskii'

_res = 'dostoevsky_pyatiknigie.txt'

g = open(_res, 'w+')

for filename in glob.glob(os.path.join(path, '*/*.txt')):

  f = open(filename, 'r')

  for line in f:
    # print(line)
    g.write(line)

