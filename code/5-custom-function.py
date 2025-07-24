def hypotenuse_calculator (side_a = 1, side_b = 1): # we can assign default value
  hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
  return round (hypotenuse, 2)

print (hypotenuse_calculator (side_a = 4, side_b = 5))  
# we can pass named argument "hypotenuse_calculator (side_a = 4, side_b = 5))  so that user can know which value are we passing to which argument 
# useful when you have to deal with lots of argument


############################################################
### Exercise
# Create a "shouter" function that takes 2 arguments: A string and a number The function should print the string multiple times
# whatever is specified in the number argument) Capitalise every letter that is printed If the number is greater than 10 don't print
# the input string. Instead, print 'you are too loud' ond The function should also return the string 'done'
# and have default values
############################################################

def shouter(text='Hello', times=2):
  counter=1
  while counter<=times:
    if(times>=10):
      print('You are too loud')
      break
    else: 
     print(text.capitalize())
     counter+=1
  
  return "DONE"


status= shouter('hello john greetings', 11)
print(status)