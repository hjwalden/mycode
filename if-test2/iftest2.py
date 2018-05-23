#!/usr/bin/env python3
#Demonstration of IPv4 Testing with if
#Written by Homer Walden

#User input IP address
ipchk=input('Apply an IP address: ')

#Match IP address
if ipchk=='192.168.70.1' or ipchk=='192.168.71.1':
    print('Looks like the IP address of the Gateway was set: ' +ipchk + ' This is not recommended. ')

#If any data is provided, this will test true
elif ipchk:
    print('Looks like the IP address was set: ' + ipchk)

#If data is not provided
else:
    print('You did not provide input. ')