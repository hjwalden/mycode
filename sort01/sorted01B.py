#!/usr/bin/env python3

import time


hf=open('/home/student/mycode/sort01/sorted01.py', 'r') #open and read file and set to variable (hf); can also use hf=open('sorted01.py', 'r')
homelist=hf.readlines() #read content of variable (hf)

sorthomelist = sorted(homelist) #sort homelist in alphabetical order and place into a variable

##Display original list
print("ORIGINAL LIST:", homelist)

##Display sorted list
print("\nSORTED LIST:", sorthomelist)

##Print sorted list to a new file
filename="sorted_logfiles_" + str(time.ctime()) #create filename with time
print("\nSORTED LIST:", sorthomelist, file=(open(filename, 'w')))
print("File created.")