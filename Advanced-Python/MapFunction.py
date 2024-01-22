def even_or_odd(num):
    if num % 2 == 0:
        return f"Function {num} is Even"
    else:
        return f"Function {num} is Odd"


# How to find even or add in this list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use Map function
print(list(map(even_or_odd, lst)))
