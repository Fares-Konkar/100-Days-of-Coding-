## Day 1:

print('Hello World!')

if 5>2 :
    print('Five is grater than two!')

## Day 2:
    
# this is a comment
"""
this is also a comment 
"""
print('my name is fares')# this is another way of comminting 

## Day 3:

# assining varibles

x, y = 20, 'Ahmad' # we can assign either constant or string to a varibles
print('My name is: ' + y + " my age is: " + str(x)) # number cant be printed, it need to get transfered to string 
# we can't add string to a number:
"""print('x+y')"""


## Day 4:

# There are three type of number
"""
x= 1   >int
x= 1.0 >Float 
x= 1j  >complex 
"""
# to get the type of any number
print(type(x))
# to change types
print(float(x))
print(complex(x))
# complex can't transfer into int, float
# there is a packege called random that create a random number
import random
print(random.randrange(1,10))







