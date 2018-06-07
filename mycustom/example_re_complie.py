#!/usr/bin/env python3


import re

#mytxt=open ('name of file or path to file') #r is implied
mytxt=open ('C:\\python36\\longbook.txt')

alllines=mytxt.readlines()

mytxt.close()

lookingfor = re.compile(r'smi[lt]e\w*')

for oneline in alllines: #oneline represents each line in the alllines
    mymatchogl = lookingfor.search(oneline)
    if mymatchobj: #if this has a value then print; if not move to the next line through storylines
        print(mymatchobj.group(), '***', oneline, end='')