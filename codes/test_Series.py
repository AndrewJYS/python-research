import pandas as pd

a = pd.Series([2,4,6,8])
print(a.values) # [2 4 6 8]
print(a.index) # RangeIndex(start=0, stop=4, step=1)

a = pd.Series([2,4,6,8], index=['a', 'b', 'c', 'd'])
print(a.values) # [2 4 6 8]
print(a.index) # Index(['a', 'b', 'c', 'd'], dtype='object')

dict = {'a':2, 'b':4, 'c':6, 'd':8}
a = pd.Series(dict)
print(a)
"""
a    2
b    4
c    6
d    8
dtype: int64
"""



print(a['a']) # 2
print(a[['a', 'd']])
"""
a    2
d    8
dtype: int64
"""

a.index = ['e', 'a', 'b', 'c']
print(a)
"""
dtype: int64
e    2
a    4
b    6
c    8
dtype: int64
"""