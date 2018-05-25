#!/usr/bin/env python3
#Parsing Log Files
#Written by Homer Walden

loginsuccess=0
loginfail=0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r') #create file object for desired file
keystone_file_lines=keystone_file.readlines() #create a list where each item is a line from the file

#Start for loop
for i in range(len(keystone_file_lines)): #sets range as total number of lines in original file
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

    elif "-] Authorization failed" in keystone_file_lines[i]:     
        loginsuccess += 1 # this is the same as loginsuccess = loginsuccess + 1
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(loginsuccess))