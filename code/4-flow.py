
############################################################
# if and elif statement 
############################################################
if 2>4:
  print('correct result')
elif 4>2:
    print('correct result again')
    if(len([1,2,3])> 2):
       print('list is long enough')
else:
  print('Incorrect result')  

############################################################
#  while loop
############################################################

counter=0
while counter<=10:
   print(counter)
   counter+=1

   if(counter==5):
      print('Counter is 5 right now')

print('---while loop has finished---')

################################################
#  for loop this loop can be iterrate on any container data type (like tuples, sets, lists, dictionary)
############################################################
print('---For loop has Started---')

# test_var=(1,2,3.1234, 'a-string') # touple
test_var=[1,2,3,4,5,6,7] #list
# test_var={1,2,3,3,2,3,1} #sets (only return 1,2,3)
for x in test_var:
   print(x)
  
# NOTE: for dictionary to run this you need to "for key, value in test_var.items():" it will return both key and value bcz by default it return only key
test_dict={'age':23, 'name':'John', 'salary':'$3200'} 
for key,value in test_dict.items():
   print(key, value)


############################################################
# Truthy and falsy
############################################################
#NOTE: Truthy & Falsy is automatic conversion to boolean. Empty Container, string w/o letters and 0 are false & everythng else is truthy for Ex

if(1):{
   print('1 is truthy its has value')
} 
   
   
   
############################################################
# EXERCISE 
# Create a list = (1,2,3,4,5) and run code for every item, If the value is 2 print "the value is 2"
# If it isn't print "the value is not 2"
# If the value is 5 run a while loop to print 'last item' 5 times
############################################################

a_list=[1,2,3,4,5]
print(a_list[len(a_list)-1])


for x in a_list:
   if(x==2):
      print('the value is 2')
   if( x==5):
      counter=0
      while counter <=5:
         print('last-item :', a_list[len(a_list)-1])
         counter+=1 
   else:
      print('the value isnot 2')



