list1 = [1, 2, 3, 4, 5, 6]

# get alternate items from list
#print(list1[0::2])

# print reverse list
#for n in range(len(list1) - 1, -1, -1):
#    print(list1[n])

# -----------------------------List comprehension-----------------------------
l1 = [i for i in range(1,50) if i%2==0]
print(l1)

s='Rohit Shrivastava'
list2 = [a for a in s]
print(list2)