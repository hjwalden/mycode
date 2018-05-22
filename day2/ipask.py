#!/usr/bin/env python3
# This script is used to collect a user's IP and MAC address and store each into a variable.
# Written by Homer Walden

#prompt user for IP address
print('What is your IP address?') 
hwip = input() #user IP address input


#prompt user for MAC address
print('What is your MAC address?') 
hwmac= input() #user MAC address input


#print fn of user's IP and MAC address
print('You said your IP address is ' + str(hwip) + ' and your MAC address is ' + str(hwmac)) 
