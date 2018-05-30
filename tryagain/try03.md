#!/usr/bin/env python3
##Lab 39 - Try and Except Part 3
##Written by Homer Walden

try:                                                          ##try this code
    print('Type the name of the configuration file to load.') ##print string
    configfile = input('Filename: ')                          ##make input a variable named configfile
    configfileobj = open(configfile, 'r')                     ##open and read variable configfile and place results into variable configfileobj, usin open function and read parameter
    switchconfig = configfileobj.read()                       ##open and read variable configfileobj and place results into variable switchconfig but using read as a method
    x = 'Switch config file found.'
except:                                                       ##if there is an exception do the following
    x = 'General error with obtaining configuration file!'
else:                                                         ##if no exceptions exist do the following
    configfileobj.close()                                     ##close configfileobj
finally:                                                      ##upon exiting the script do the following
    print('\n\nWriting results of routine to log file')       ##print string
    print(x)                                                  ##code to write value of x to log file
