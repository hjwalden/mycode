#!/usr/bin/env python3
#Exploring Network Interfaces
#Written by Homer Walden

import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') #Label MAC address without newline
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #Prints MAC Address
        print('IP: ', end='') #Label IP Address without newline
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #Prints IP address
    except:
        print('Could not collect adapter information') # Print an error message