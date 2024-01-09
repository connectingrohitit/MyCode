set1 = {1, 2, 3, 4, 5}
list1 = ['Rohit', 'Shri', 'Vastava', 'VC']

set2 = set(list1)
print(set1)
print(set2)
print(set1.pop())
print(set2.remove('VC'))
print(set1)
print(set2)
print((set1.discard(5)))
print(set1)
set1.update(list1)
print(set1)