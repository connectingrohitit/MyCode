def sumnum(a, b=6):
    return a + b


print(sumnum(2))
print(sumnum(2, 5))


def evenoddsum(*args):
    even_sum = 0
    odd_sum = 0
    for i in args:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum


print(evenoddsum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
