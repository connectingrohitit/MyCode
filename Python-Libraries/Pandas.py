import pandas as pd
import numpy as np

# Create data frame
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'],
                  columns=['Col1', 'Col2', 'Col3', 'Col4'])
print(df)


# Access the elements / items using loc
print(df.loc['Row1'])
# check the type i.e. data series
print(type(df.loc['Row1']))

# Access the elements / items using iloc
print(df.iloc[0:2, 0:3])
# check the type i.e. data frame
print(type(df.iloc[0:2, 0:3]))

# convert data frame into array
print(df.iloc[0:2, 0:3].values)

# check null values in a data frame
print(df.isnull().sum())

# check repetition of an item in a column of data frames
print(df['Col1'].value_counts())

# get unique values in a column
print(df['Col1'].unique())