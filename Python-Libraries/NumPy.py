import numpy as np

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [2, 3, 4, 5, 7]
my_list3 = [10, 20, 30, 40, 50]
arr = np.array([my_list1, my_list2, my_list3])
print(arr)
print(type(arr))
# how many rows and columns
print(arr.shape)
# 5 rows, 3 columns
print(arr.reshape(5, 3))
print(arr)
# total elements
print(arr.size)
# retrieve specific elements
print(arr[0:3, 4:5])

# create a new array with numbers in a range
ar1 = np.arange(0,10)
print(ar1)
# create a new array with numbers and interval in a range
ar2 = np.arange(0,20, 3)
print(ar2)


# Get number of items in a range
print(np.linspace(1, 50, 20))

# check values
val = 5
print(arr[arr<val])

# get random int values
print(np.random.randint(0, 100, 5))

