# Methods that start with 'Double Underscore' are called 'Dunder' or 'Magic Methods' in python
# These methods are internal methods and can be accessed/seen using dir(<object>/class) command e.g. dir(datetime)


import time
from datetime import datetime

time_format = '%H:%M:%S'
start_time = datetime.now()
time.sleep(2)
end_time = datetime.now()
execution_time = end_time - start_time

print(start_time)
print(end_time)
print(execution_time)
