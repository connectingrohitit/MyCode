import pandas as pd
from io import StringIO
# read csv
df = pd.read_csv('Data.csv')
print(df)

# read csv with a different separator e.g. ;
df2 = pd.read_csv('Data2.csv', sep=';')
print(df2)

# Reading using StringIO
df3 = pd.read_csv(StringIO('Data.csv'), usecols=['Col1', 'Col3'])
print(df3)