#!/usr/bin/env python3
##Update SW2 config file
##Written by Homer Walden

from napalm import get_network_driver # import code from NAPALM
driver = get_network_driver('eos') # get hte driver for Arista devices
device = driver('172.16.2.20', 'admin', 'alta3') # apply the switch credentials
device.open() # start the connection
#The next two lines of code are new
device.load_merge_candidate("/home/student/mycode/napalm/merge.me")
device.commit_config()