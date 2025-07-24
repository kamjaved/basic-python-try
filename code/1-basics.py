# --EXECUTION ORDER---- top to bottom
print('line-1')
print('line-3')
print('line-2')

#---DATATYPES----
print('words in single quotes') # STRING you can use either single or double quotes 
print("words in double quotes")
print ('INTEGER', 123) # INTEGER or ints
print(-10) # NEGETIVE VALUE
print('FLOATS', 1.2) # Float point or float (python treats integer and float differently)

# ----OPERATIONS----

print(3+3) # ADD
print(3-3) # SUBSTRACT
print(3*3) # MULTIPLY
print(3/3) # DIVIDE
print(10 + 0.1356348773) # you can add INT & FLOAT together 
#print(10 + 'hello')  # This is not possible and gives you TypeError
print(10 * ' hello')  # it will print hello 10 times 
print(13-3 * (4+2)) # more precise calculation parenthesis will handles forst then multiplication then substraction Output -5

# VARIABLES

test_value=123
test_value += 50
print(test_value) # prints 173 

#BEST RACTICE TO DECLARE VARIABLE
# Variable names
# Mandatory
# only letters A-z & 0-9 + -
# cannot start with a number (1test is invalid)
# Case sensitive (test123 is different from Test123)
# Cannot use names of inbuilt functions (print)
# Be clear with variable names
# Use snake_case
# Default

#INPUT

num_1= input('Please enter your first Number: ')
num_2= input('Please enter your second Number: ')

print('Your Total Sum is :', int(num_1)+int(num_2))
