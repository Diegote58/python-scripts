
# Python3 code to demonstrate  
# to get random number from list 
# using random.choice() 
import random 
  
# initializing list  
test_list = [1, 4, 5, 2, 7,2,3,4,5,6,7,8,9,0] 
  
# printing original list  
print ("Original list is : " + str(test_list)) 
  
# using random.choice() to  
# get a random number  
random_num = random.choice(test_list) 
  
# printing random number 
print ("Random selected number is : " + str(random_num)) 

names = ['Sam', 'Paul', 'Mark', 'Simon', 'Sean', 'Samantha', 'Ellen']
print(random.choice(names))

random_items = random.choices(population=names, k=len(test_list))
print(random_items)