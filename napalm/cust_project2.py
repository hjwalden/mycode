#!/usr/bin/env python3
##NAPALM Exercises
##Written by Homer Walden

from napalm_testing import eddiebabe
from datetime import datetime

answer='yes'
while(answer !='q'):
    x=input("What driver are we using? ")
    y=input("What is the IP address? ")
    u=input("What is the username? ")
    p=input("What is the password? ")
    z=eddiebabe(x, y, u, p)
    filename="current_cfg_" + str(datetime.now)
    hwfile=open(filename, "w")
    print("You told me the driver was " + str(x) + " and the IP address was " + str(y) + " who has a running config of " + str(z), file=hwfile)
    answer=input("go again? q to quit")
