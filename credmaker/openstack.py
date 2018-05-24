#!/usr/bin/env python3
#Outputting Data to Files
#Writted by Homer Walden

#Open a file
outFile = open('admin.rc', 'a')

#Prompt the user for the OS_AUTH_URL, and then write it to admin.rc
print('What is the OS_AUTH_URL?')
osAUTH = input()
print('export OS_AUTH_URL=' + osAUTH, file=outFile)

#Write file to admin.rc
print('export OS_IDENTITY_API_VERSION=3', file=outFile)
print('What is the OS_PROJECT_NAME?')
osPROJ = input()

#Prompt the user for the OS_PROJECT_NAME, and then write it to admin.rc
print('export OS_PROJECT_NAME=' + osPROJ, file=outFile)
print('What is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()

#Prompt the user for the OS_PROJECT_DOMAIN_NAME
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outFile)

#Prompt the user for the OS_USERNAME
print('What is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME=' + osUSER, file=outFile)

#Prompt the user for the OS_USER_DOMAIN_NAME
print('What is the OS_USER_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outFile)

#Prompt the user for the OS_PASSWORD
print('What is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD=' + osPASS, file=outFile)

#Close the file admin.rc
outFile.close()