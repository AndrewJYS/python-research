import pandas as pd
import numpy as np

data = [[11,22,33],[44,55,66],[77,88,99]]
frame = pd.DataFrame(data, columns=['a','b','c'], index=['1','2','3'])
print(frame)

data = np.array([[11,22,33],[44,55,66],[77,88,99]])
frame = pd.DataFrame(data, columns=['a','b','c'], index=['1','2','3'])
print(frame)

data = {'a': [11,44,77], 'b': [22,55,88], 'c': [33,66,99]}
frame = pd.DataFrame(data, index=['1','2','3'])
print(frame)
"""
    a   b   c
1  11  22  33
2  44  55  66
3  77  88  99
"""

print(frame['a'])
"""
1    11
2    44
3    77
Name: a, dtype: int64
"""

print(frame[['a', 'c']])
"""
    a   c
1  11  33
2  44  66
3  77  99
"""

print(frame.loc['1'])
"""
a    11
b    22
c    33
Name: 1, dtype: int64
"""


# 定义数据
data = {'a': [11,44,77], 'b': [22,55,88], 'c': [33,66,99]}
frame = pd.DataFrame(data, index=['1','2','3'])

# 存储数据
frame.to_csv(f'test.csv')

# 读取数据
dat = pd.read_csv(f"test.csv")
print(dat)
"""
   Unnamed: 0   a   b   c
0           1  11  22  33
1           2  44  55  66
2           3  77  88  99
"""

dat = pd.read_csv(f"test.csv", index_col=0)
print(dat)
"""
    a   b   c
1  11  22  33
2  44  55  66
3  77  88  99
"""


