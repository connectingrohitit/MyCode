d = {
    'name': 'Rohit Shrivastava',
    'age': 38,
    'profile': 'Engineering Manager'
}

print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))
# d.__delitem__('age')
# print(d)
# d.__reversed__()
# print(d)
d['now'] = 'Coding in Python'
d['age'] = 40
d.update({'age': 39})
for a, b in d.items():
    print(a, b)
