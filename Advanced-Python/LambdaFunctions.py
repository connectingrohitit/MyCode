# Lambda functions are anonymous function or Function with no name
# A function with single expression (line of code) inside a function can be converted to lambda function

addition = lambda a, b: a + b
print(addition(2, 3))

even = lambda a: a % 2 == 0
print(even(12))
