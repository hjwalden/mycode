#!/usr/bin/env python3
#Manipulation of Mix Lists
#Written by Homer Walden

#Create and display list of protocols
proto=['ssh', 'http', 'https']
print(proto)

#Prints 2nd item in the list
print(proto[1])

#Extends 'dns' to end of list
proto.extend('dns')
print(proto)

#Appends 'dns' to end of list
proto.append('dns')
print(proto)

#Create new list of common ports
proto2=[22, 80, 443, 53]

#Pass proto2 as an argument to the extend method, then print
proto.extend(proto2)
print(proto)

#Pass proto2 as an argument to the append method, then print 
proto.append(proto2)
print(proto)

#Reverse the elements of the list
proto.reverse()
print(proto)

