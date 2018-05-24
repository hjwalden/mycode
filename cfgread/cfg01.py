#!/usr/bin/env python3
#Explore Read and Readlines from a file
#Written by Homer Walden

#Create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

#Display file to the screen - .read()
print(configfile.read().strip())

#Close file
configfile.close()

#Re-create file object to explore new method
configfile = open('vlanconfig.cfg', 'r')

#Make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

#Iterate through configlist and print results without '\n'
for x in configlist:
    print(x.strip())

#Close the file
configfile.close()