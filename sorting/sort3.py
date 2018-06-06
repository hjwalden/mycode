#!/usr/bin/env python3
##Create a function to return positions in a list
##Written by Homer Walden

##Create a tuple
simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]

##Create a fn to return 1st position of tuples in a list
def sortage(x):
    return x[1] #pass x and return 1st position

print("The results of sorted(simpsons, key=storage):", sorted(simpsons, key=sortage))
#maggie, lisa, bart, marge, homer