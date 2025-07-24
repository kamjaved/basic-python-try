# TUPLE = ('bob', 123, 'Lisa', ('another list') )

a_tuple=(1,2,3.1234, 'a-string')
print(a_tuple)

# LIST = ['bob', 123, 'Lisa', ('another list*')]

a_list=[1,2,3,'a-string']
a_list.append('abother word')
print(a_list)
# Difference between TUPLE () and LIST [] and then comma separated values &  A tuple cannot change (immutable) while you can modify the values of a list

# SET = {1,2,3, 'test'} Every entry is unique
a_set={1,2,3,3,1,2,4,4}
print(a_set)

# DICTIONARY = {'name': 'Bob', 123: 'test, 'Lisa /2)}
# Key: value pairs instead of single entries like JS Objects

a_dictionary={'name': 'John Doe', 'age':'25', 123: ['James Bond', 1,2,3]}

print(a_dictionary)
print(a_dictionary['name'], 'is',  a_dictionary['age'], 'year old')



# HOW TO GET VALUES FROM CONTAINERS

user_list=['Lisa', 'John', 'Bob', 'Anna', 'Alex', 'Greg', 'Michal', "Watson"]
print(user_list[0:7:2])

#EXERCISE print (8,6,4,2)
numbers=[1,2,3,4,5,6,7,8,9,10]
# print('start': 'end', 'step')
print(numbers[7 : 0 : -2])
