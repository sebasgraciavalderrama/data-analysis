import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})


print(df['col2'].unique()) # List of unique values
print(df['col2'].nunique()) # Number of unique values
print(len(df['col2'].unique())) # Number of unique values
print(df['col2'].value_counts()) # How many times does that value occur in that column

print(df[(df['col1']>2) & (df['col2']==444)]) # Conditional selection

def times2(x):
    return x*2

# How to apply previous function (custom functions) to columns
print(df['col1'].apply(times2))

# How to apply built-in functions to columns
print(df['col3'].apply(len))

# Lambda expressions
print(df['col2'].apply(lambda x: x*2))

# Removing columns
print(df.drop('col1', axis=1))

print(df.columns)
print(df.index)

# Sorting and ordering
print(df.sort_values(by='col2'))
print(df.sort_values(by='col1'))

# Find null values
print(df.isnull())

# Pivot table
data = {'A':['foo', 'foo', 'foo', 'bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x', 'y', 'x', 'y', 'x', 'y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print(df)
print('\n')
pivot_df = df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
print(pivot_df)
