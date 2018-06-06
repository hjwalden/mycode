#!/usr/bin/env python3
##Written by Homer Walden
##Goal: experiment with the utilization of the sorted function

##Create a list
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

##Print current list
print("Currently the value of vendors:", vendors)

##Sort list in alphabetical order using sorted fn
print("\nThe results of sorted() function:", sorted(vendors))

##Reprint list after sort to show the values of the list hasn't changed
print("\nBut the value of the list hasn't actually changed:", vendors)

##Create a sorted list in alphabetical order
sortedvendors = sorted(vendors)
print("\nOur sorted vendor list looks like this:" + str(sortedvendors))

##Reverse alphabetical order of the sorted list
baksortvendors = sorted(vendors, reverse=True)
print("\nOur sorted vendor list looks like this:", baksortvendors)

##Create a mix list of lower and capitals
vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', 'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

##Print list
print("\nOur new vendordeux list looks like this: ", vendorsdeux)

##Sort list in alphabetical order using sorted fn
print("\nOur sorted vendor list looks like this: ", sorted(vendorsdeux))