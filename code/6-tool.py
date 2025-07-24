###############################################

# F String
###############################################

user_name= 'John'
user_age=25
bad_approach= user_name + ' is ' + str(user_age) + ' years old'
good_approach= f'{user_name} is {user_age+10} years old'

print(bad_approach)
print(good_approach)

###############################################
#  Single line IF sttements
###############################################
user_age=14
user_status = 'Adult' if user_age>=18 else 'Child'
print (user_status)


###############################################
# LIST COMREHENSION

# list comprehension see the lamda-and-list-comp.md for more explanation & examples
# ist comprehension is a shorter and more readable way to create new lists
# by looping over an iterable (like a list, range, or string) in a single line.
###############################################

# prints only unique number
unique = {x%3 for x in range(10)}
print(unique) # Since we're using (%3), the possible remainders can only be 0, 1, or 2. Let's see how this works:
# 0 % 3 = 0
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1
# And so on...


# prints only even number
evens= [ x for x in range(11) if x%2==0]
print(evens)

#  EXERCISE-1
# Create a list of all numbers between 1 and 20 that are divisible by both 3 and 5 (whihc is 15), and store "FizzBuzz" instead of the number.
def multiple(number):
  return 'Fizzbuzz' if number%3==0 and number%5==0 else number

fizzbuzz= [multiple(num) for num in range(1,21, 1) ]
print(fizzbuzz)

#  EXERCISE-2
# create a combination of letters and number in range if lettes A,B given and number 1,2 is given 
# like A1,A2,B1,B2

row_column= [f'{col}{row}' for col in ('A', 'B', 'C', 'D') for row in range(1,5)]
print(row_column)

###############################################
#### LAMBDA FUNCTION (lke arrow function in JS (not exactly but you can relate ))
# Expression: lambda arguments: expression
# more example and explanation in lamda-and-list-comp.md
###############################################

multiply_two = lambda x: x*2
print(multiply_two(2))  # 4

# we can also call lambda function immediatly like IIFEE in JS
multiply_two_iife = (lambda x: x*2)(2)
print('IIFE', multiply_two_iife)  # 4


number_list=[i for i in range(1,21)]
filtered_list=list(filter(lambda i: i%2==0,number_list))
print(filtered_list)

age_category= lambda age: 'Adult' if age>=18 else 'Minor'
print(age_category(19))



