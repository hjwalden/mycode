#!/usr/bin/env python3
# Experimenting with lists and mixed data types
# Written by Homer Walden

#create new list of mixed data types
my_list=["192.168.0.5", 5060, "UP"]

#display IP address
print("The first item in the list (IP): " + my_list[0]) 

#display port number
print("The second item in the list (port): " + str(my_list[1]))

#display current status
print("The last item in the list (state): " + my_list[2]) 

#create a new list of mixed data types
new_list=[5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#display list of mixed data types
print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + ", I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) + ".")