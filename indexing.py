import numpy as np

arr = np.array([20, 40, 60, 80, 90])

# I want to access the item of index 2
# In python arrays indexes start from 0

print(arr[2])  #it will print 60
print(arr[3])  #it will print 80

# There is also a concept of Slicing
#Slicing is used where we want to access of part of array

print(arr[1:3]) #it will start from index 1 and end before 3 
#3 index will not be included


#we can also use neagtive indexing

print(arr[-1]) #it iwll print 90