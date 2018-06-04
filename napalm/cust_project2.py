#!/usr/bin/env python3
##NAPALM Customization Project
##Written by Homer Walden

##Import created function
from napalm_testing import hwnapalm

##Import datetime
from datetime import datetime

answer='yes'
while(answer !='q'):                       #creates loop until user types 'q' to quit                       
    x=input("What driver are we using? ")  #user input driver type

    y=input("What is the IP address? ")    #user input IP address

    u=input("What is the username? ")      #user input login for driver

    p=input("What is the password? ")      #user input password for driver

    z=hwnapalm(x, y, u, p)                 #results from imported function

    filename="current_config_" + str(datetime.now()) #create filename

    hwfile=open(filename, "w") #create file with user input and results from function

    print("Driver: " + x + "\n" + "\nIP address: " + str(y) + "\n" + "\nRunning config: " + str(z['running'] + "\n"), file=hwfile) #prints info to newly created file

    print("Config file created.")    
    hwfile.close()
    answer=input("go again? q to quit")