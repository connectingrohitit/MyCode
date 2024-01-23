# Adding exception type 'NameError' on top of generic Exception
try:
    a = b
except NameError:
    print("A variable is not defined")
except Exception as ex:
    print(ex)

# Adding exception type 'NameError & TypeError' on top of generic Exception
try:
    a = 1
    b = 'Rohit'
    c = a + b
except NameError:
    print("A variable is not defined")
except TypeError:
    print("Data types are not similar")
except Exception as ex:
    print(ex)

# Adding exception types on top of generic Exception and using 'else'
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a / b
except NameError:
    print("A variable is not defined")
except TypeError:
    print("Data types are not similar")
except ZeroDivisionError:
    print("Please provide 2nd number greater than zero.")
except Exception as ex:
    print(ex)
else:
    print(c)

# Adding exception types on top of generic Exception and using 'else' & 'finally'
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a / b
except NameError:
    print("A variable is not defined")
except TypeError:
    print("Data types are not similar")
except ZeroDivisionError:
    print("Please provide 2nd number greater than zero.")
except Exception as ex:
    print(ex)
else:
    print(c)
finally:
    print('Execution over')
