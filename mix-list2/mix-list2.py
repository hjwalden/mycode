#!/usr/bin/env python3
#Lab 09 - Mix List 2
#Written by Homer Walden

#create and display list of protocols
proto=['ssh', 'http', 'https']
print(proto)

#print 2nd item in the list
print(proto[1])

#this line will extend 'dns' to end of list
proto.extend('dns')
print(proto)

#this list will append 'dns' to end of list
proto.append('dns')
print(proto)

#create new list of common ports
proto2=[22, 80, 443, 53]

#pass proto2 as an argument to the extend method, then print
proto.extend(proto2)
print(proto)

#pass proto2 as an argument to the append method, then print 
proto.append(proto2)
print(proto)

#reverse the elements of the list
proto.reverse()
print(proto)

