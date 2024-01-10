# Use of mypy module to validate expected data type for parameters as well as return type
def myfunc(param: int) -> str:
    return param


print(myfunc(10))