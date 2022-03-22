import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels)) #print(pd.Series(my_data,labels))
print(pd.Series(d))
print(pd.Series(labels))
print(pd.Series(data=[sum, print, len]))

ser1 = pd.Series([1,2,3,4],['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser1)
print(ser2)

#Operations with Series

ser3 = ser1 + ser2
print(ser3)