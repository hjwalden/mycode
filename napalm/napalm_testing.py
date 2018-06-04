#!/usr/bin/env python3
##NAPALM Exercises
##Written by Homer Walden

##Import code from NAPALM
from napalm import get_network_driver

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