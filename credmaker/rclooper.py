#!/usr/bin/env python3
#Outputting Data to Files
#Written by Homer Walden


import csv                    #import excel spreadsheet as a .CSV file
f=open('csv_users.txt','r')   #create variable (f) to readh file csv)users,txt
i=0                           #counter

#Read each line of the csv as a row and print to each specified file
for row in csv.reader(f):
    i=i+1
    filename='admin.rc%d'%(i,)
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + row[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile)
    print('export OS_USERNAME=' + row[3], file=rcfile)
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)
    print('export OS_PASSWORD=' + row[5], file=rcfile)
    rcfile.close()