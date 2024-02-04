#print 
print ("hello world")
#variables
hello=11
re=2000000.2
print(re)
#operator precedence
print (2+3*6)
#boolean operators
print (True and True,True and False,False and True, False and False)
print (True or True,True or False, False or True, False or False)
print (not True)
#conditionals
name="bluestreetisacamelcasewalk"
name=int( input("what is your guess? "))
import random 
secret_number=random.randint(1,100)
while True:
  if name < secret_number:
    print ("The number you are attemting to guess is larger than your guess" )
    name=int( input("what is your guess? "))    
  elif name> secret_number:
    print ("The number you are attempting to guess is smaller than your guess")
    name=int( input("what is your guess? "))    
  else: 
    print("yay! you guessed correctly! congratulations!!!")
    break
    