# Create list using list comprehension

# Typical way of creating is by using append in loop e.g.
# lst1 = []
#
#
# def lst_square(lst):
#     for i in lst:
#         lst1.append(i * i)
#     return lst1
#
#
# print(lst_square([1, 2, 3, 4, 5]))

# Now doing the same thing using "List Comprehension"
lst = [1, 2, 3, 4, 5]
lst1 = [i * i * i for i in lst]
#lst1 = [i * i * i for i in lst if i%2 ==0]
print(lst1)
