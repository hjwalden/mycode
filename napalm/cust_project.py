#!/usr/bin/env python3
##NAPALM Exercises
##Written by Homer Walden

##Import code from NAPALM
from napalm import get_network_driver

##Import datetime 
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
    x=input("What driver are we using? ")  #user input driver type
    y=input("What is the IP address? ")    #user input IP address
    u=input("What is the username? ")      #user input login for driver
    p=input("What is the password? ")      #user input password for driver
    z=eddiebabe(x, y, u, p)                #results from function
    filename="current_config_" + str(datetime.now) #create filename
    hwfile=open(filename, "w") #create file with user input and results from function
    print("Driver: " + x + " IP address: " + str(y) + " Running config: " + str(z), file=hwfile) #writes info to file
    print("Config file created.")    
    answer=input("go again? q to quit")
