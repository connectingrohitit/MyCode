# ---------------------------- Reading nested dictionary ------------------------
members = {
    'father': {'name': 'Rohit', 'age': 39, 'weight': 64},
    'mother': {'name': 'Garima', 'age': 39, 'weight': 72},
    'child': {'name': 'Ritvika', 'age': 5, 'weight': 25},
}
for k, v in members.items():
    print(k)
    for i, j in v.items():
        print(i, j)
