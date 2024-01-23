# Used for huge list of values. Iterators are not initialized in the memory. Only 1 value gets initialized at a time
# that too when we call next() function
# so it saves run time memory consumption in case of huge list

# List is an iterable. It can be converted to Iterators using iter() function
my_list = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

print((next(my_iter)))
print((next(my_iter)))
print((next(my_iter)))
print((next(my_iter)))
