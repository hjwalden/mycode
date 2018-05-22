#!/usr/bin/env python3
#Lab 10 - Lists of Lists
#Written by Homer Walden

#Create a list of network devices then print
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

#Display second item in list
print(list1[1])

#Extend an item to the list
list1.extend(['juniper'])
print(list1)

#Append a list within the list1
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)

#Display item 5 within list1
print(list1[4])

#Print 1st IP address from list
print(list1[4][0])