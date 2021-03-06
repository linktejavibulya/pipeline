#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:43:43 2019

@author: Or Duek
small script that will remove (MB4iPAT2) from filename
Script was replaces and merged with creatBIDS.py

"""

import os
from bids import BIDSLayout

data_dir = '/media/Data/rcfTest'
#data_dir = '/media/Data/kpe_forFmriPrep'

layout = BIDSLayout(data_dir)
layout.get_sessions()
layout.get() #, extension='nii.gz')[0].filename

# maybe need to change the way we look for all bold files with these parenthases

for i in source_epi:
    a = i.filename
   # print (i.filename)
    if a.find('(MB4iPAT2)')!=-1:
        print ("We have found an issue with ", a)
        b = a.split('(MB4iPAT2)') # this is the part that will be omitted from the file name. If you have an extra - you should add that too. 
        c = b[0] + b[1] # cmobine toghether
        #change filename
        os.rename(a, c)
