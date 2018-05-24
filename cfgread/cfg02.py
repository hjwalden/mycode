#!/usr/bin/env python3
#Reading from a File
#Written by Homer Walden

#Create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

#Display file to the screen - .read()
print(configfile.read())
configblog = configfile.read()

#Break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

#Display list without '\n'
print(configlist)

#Close the file
configfile.close()