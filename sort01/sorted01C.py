#!/usr/bin/env python3
##Written by Homer Walden
##Lab 69 - Getting sorted()
##Goal: Open and read a file then sort file content and print content into a new file

import time

##Open and read file and set to variable (hf); can also use hf=open('sorted01.py', 'r')
##Read content of variable (hf)
hf=open('/home/student/mycode/sort01/sorted01.py', 'r')
homelist=hf.readlines()

##Sort homelist in alphabetical order and place into a variable
sorthomelist = sorted(homelist)

##Display original list
print("ORIGINAL LIST:", homelist)

##Display sorted list
print("\nSORTED LIST:", sorthomelist)

##Print sorted list to a new file
filename="sorted_logfiles_" + str(time.ctime()) #create filename with time
print("\nSORTED LIST:", sorthomelist, file=(open(filename, 'w')))
print("\nFile created.")