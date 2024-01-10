# Code to calculate execution timing of a function
from _datetime import datetime


def timed(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        value = function(*args, **kwargs)
        end_time = datetime.now()
        execution_time = (end_time - start_time).seconds
        f_name = function.__name__
        print(f"Function {f_name} took {execution_time} seconds to execute.")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for n in range(1, x):
        result *= n
    return result


myfunction(100000)
