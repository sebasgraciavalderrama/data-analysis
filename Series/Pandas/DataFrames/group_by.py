import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
by_comp = df.groupby('Company')
print(by_comp.mean())
print(by_comp.sum())
print(by_comp.std())
print(by_comp.sum().loc['FB'])
# --- One liner
print(df.groupby('Company').sum().loc['FB'])
# --- Count
df.groupby('Company').count()
# --- Max
df.groupby('Company').max()
# --- Min
df.groupby('Company').min()
# --- Describe method
df.groupby('Company').describe()#.transpose()['FB']
