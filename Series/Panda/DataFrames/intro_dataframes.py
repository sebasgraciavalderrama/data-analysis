import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'])
print(type(df['W']))
print(type(df))
print(df.W) # Don't use this
print(df[['W', 'Z']])

# ----- Create a new column (new serie) in the DataFrame
df['NEW'] = df['W'] + df['Z']
print(df)
# ----- Delete a column from the DataFrame
# The drop method returns a copy of the original DataFrame with the deleted column.
# If you want to delete the column of the actual DataFrame object you must use the inplace parameter, like this:
# df.drop('name_of_the_column', axis=1, inplace=True)
new_df = df.drop('NEW', axis=1)
print(new_df)
df.drop('NEW', axis=1, inplace=True)
print(df)
# ----- Delete a row from the DataFrame
df.drop('E', axis=0, inplace=True)
print(df)
# ----- Shape of the DataFrame
print(df.shape) # Tuple
# ----- Selecting columns
print(df['Y'])
print(df[['Y', 'Z']])
# ----- Selecting rows
print(df.loc['A'])
print(df.iloc[0])
# ----- Selecting subsets of rows/columns
print(df.loc['B','Y']) # Slicing
print(df.loc[['A', 'B'], ['W', 'Y']]) # Slicing


