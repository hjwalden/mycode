#!/usr/bin/env python3
#Pushing commands to devices
#Written by Homer Walden

#Function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )

        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )

#Start our script and replace data stored in file
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

print("Welcome to the network device command pusher") # welcome message

#Replace with function call that reads in data from file
print("\nData set found\n")

#Call function to push commands to devices 
commandpush(work2do) # call function to push commands to devices