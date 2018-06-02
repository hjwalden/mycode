#!/usr/bin/env python3
##Creating Function
##Written by Homer Walden

import datetime
import time
import os

def logarchive():
    nowtime = str(datetime.datetime.now())
    logname = "log_" + nowtime + ".old"
    os.rename("/home/student/log.txt","/tmp/log/" +logname)

###################################################

