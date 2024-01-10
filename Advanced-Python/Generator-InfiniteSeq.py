# Infinite sequence

def infinite_seq():
    result = 1
    while True:
        yield result
        result += 1


value = infinite_seq()
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
