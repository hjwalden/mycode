#!/usr/bin/env python3
##NAPALM Exercises
##Written by Homer Walden

##Import code from NAPALM
from napalm import get_network_driver

from datetime import datetime

##Create a function to automate NAPALM commands
def eddiebabe(xdriver, yIP, hwuser, hwpswd):
    
    #Tell NAPALM to speak "xdriver" commands to our switches
    driver=get_network_driver(xdriver)

    #Input switch credentials
    device=driver(yIP, hwuser, hwpswd)
    
    #Equates to: ssh into the switch, login, and enable
    device.open()

    #Get device startup and running configs
    return device.get_config()

answer='yes'
while(answer !='q'):
    x=input("What driver are we using? ")
    y=input("What is the IP address? ")
    u=input("What is the username? ")
    p=input("What is the password? ")
    z=eddiebabe(x, y, u, p)
    filename="current_config_" + str(datetime.now)
    hwfile=open(filename, "w")
    print("You told me the driver was " + str(x) + " and the IP address was " + str(y) + " who has a running config of " + str(z), file=hwfile)
    answer=input("go again? q to quit")
