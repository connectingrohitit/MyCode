import pandas as pd

# Read Json to CSV
Data = {"emp_name":"Rohit", "email":"test@gmail.com"}
print(pd.read_json(str(Data)))

