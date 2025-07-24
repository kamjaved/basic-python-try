height=int(input("Enter the hieght of the triangle: "))
base=int(input("Enter the base of the triangle: "))

hypo= float((height **2 + base ** 2) ** 0.5)

# ALTERNATE APPROACH hypo= pow(height,2) + pow(base , 2)
print('The Hypotenuse of the traingle is ', hypo)
# when you want to limit the decimal to 2 digit 
print('The Hypotenuse of the traingle is ', round(hypo, 2))

# Methods: fucntions of datatypes
#  behave just like function but its only called for datatype like we are calling for strng below some method accept argument like replace method does and some not
print('value'.upper())  # convert string to uppercase value
print('VALUE'.lower())  # convert string to lowercase value
print('value'.replace('e','3'))  # replace "e" with "3"


