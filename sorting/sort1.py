#!/usr/bin/env python3
##Written by Homer Walden
##Goal: create

##Create a new list
coastal = ['Atlanta', 'Vegas', 'portland', 'PORTLAND', 'Portland', 'San F', 'San Jose', 'NYC']

##Print list
print('\nCurrently our confusing list looks like:', coastal)
#or print('\nCurrently our confusing list looks like: ' + str(coastal))

##Sort list in alphabetical order
print('\nWe can alphabetize our list with sorted(coastal):', sorted(coastal)) #sort in alphabetical order

##Sort list in reverse alphabetical order
print('\nWe can reverse our list with sorted(coastal, reverse=True):', sorted(coastal, reverse=True))

##Show properties did not change in list when using sorted fn
print('\nOur list has not changed:' + str(coastal))

##Modify the nature of the list, sorted fn returns a new list
##sort method changes the nature of the list (reorders list, doesn't print anything unless otherwise specified)

coastal.sort()

print('\nOur list HAS been changed with list.sort():', coastal.sort())
print(coastal)

##Sort list using length as a key
print('\nOur list can be sorited with a key=len:', sorted(coastal, key=len))

##Sort list using lower as a key
print('\nOur list can be sorted with a sorted(coastal, key=str.lower):', sorted(coastal, key=str.lower))