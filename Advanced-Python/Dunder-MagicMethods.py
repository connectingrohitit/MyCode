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
