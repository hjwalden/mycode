#!/usr/bin/env python3
##Written by Homer Walden
##Lab 70 - Custom sorted() with key
##Goal: Create a list and sort list in alphabetical orders. Sort listby character length and in reverse order

##Create a list
iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', '10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', '10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']

##Print original list
print('Currently iplist looks like this:', iplist)

##Sort list
print('\nThe results of sorted(iplist) function:', sorted(iplist))

##Show the properties of the list has not changed
print('\nBut iplist has not actually changed:', iplist)

##Sort list by character length (shortest to longest)
iplistkeyed = sorted(iplist, key=len)
print('\nResults of sorted(iplist, key=len): ' + str(iplistkeyed))

##Sort list by character length in reverse order (longest to shortest)
bakiplistkeyed = sorted(iplist, key=len, reverse=True)
print('\nResults of sorted(iplist, key=len, reverse=True): ' + str(bakiplistkeyed))