#!/usr/bin/env python3
#Create own if-logic script
#Written by Homer Walden

#Create own if-logic script using if, elif and else
message = 'You passed the class. '
print('What was your number grade?')
hwgrade = float(input())
if hwgrade >= 90:
    message = message + 'You got an A.'
elif hwgrade >= 80:
    message = message + 'You got a B.'
elif hwgrade >= 70:
    message = message + 'You got a C.'
else:
    message = 'Sorry, you did not pass the class. ' + 'You got a F.'
print(message)