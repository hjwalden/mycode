#!/usr/bin/env python3
#Scripting using Dictionaries
#Written by Homer Walden
    
#Create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}
    
#Display parts of the dictionary
print( switch['hostname'] )
print( switch['ip'] )

#Request a 'fake' key with .get() method
print( "First test - .get()" )
print( switch.get('lynx') )

#Using get method
print( "Second test - .get()" )
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

#Display value for key named version
print( "Third test - .get()" )
print( switch.get('version') )

#Display dictionary keys
print( "Fourth test - .keys()" )
print( switch.keys() )

#Display dictionary values
print( "Fifth test - .values()" )
print( switch.values() )

#Using pop method
print( "Sixth test - .pop()" )
switch.pop('version') # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

#Adding a new value to the dictionary
print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'karl08'
print( switch.keys() )
print( switch.values() )

#Adding a new value to the dictionary
print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
print( switch.keys() )
print( switch.values() )