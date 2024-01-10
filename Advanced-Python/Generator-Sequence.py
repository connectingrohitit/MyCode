# sequence of squares from 1 to 100000

def my_generator(n):
    for x in range(n):
        yield x * x


values = my_generator(100000)
print(next(values))
print(next(values))
print(next(values))
print(next(values))