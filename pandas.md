# pandas  

## Series基本操作  

Series是一维的数组型对象  

1.定义Series  

```python
a = pd.Series([2,4,6,8])
print(a.values) # [2 4 6 8]
print(a.index) # RangeIndex(start=0, stop=4, step=1)
```

2.添加索引  
下面两种方法效果相同  

```python
a = pd.Series([2,4,6,8], index=['a', 'b', 'c', 'd'])
print(a.values) # [2 4 6 8]
print(a.index) # Index(['a', 'b', 'c', 'd'], dtype='object')

dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
a = pd.Series(dict)
print(a)
"""
a    2
b    4
c    6
d    8
dtype: int64
"""
```

3.改变索引  

```python
a = pd.Series([2,4,6,8], index=['a', 'b', 'c', 'd'])
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
```

4.选择标签进行索引  

```python
# 取出某个索引对应的值
a = pd.Series([2,4,6,8], index=['a', 'b', 'c', 'd'])
print(a['a']) # 2

# 取出多个索引对应的值
print(a[['a', 'd']])
"""
a    2
d    8
dtype: int64
"""
```

## DataFrame基本操作  

1.初始化DataFramme与添加索引  
下述三种方式效果相同  

```python
data = [[11,22,33],[44,55,66],[77,88,99]]
frame = pd.DataFrame(data, columns=['a','b','c'], index=['1','2','3'])

data = np.array([[11,22,33],[44,55,66],[77,88,99]])
frame = pd.DataFrame(data, columns=['a','b','c'], index=['1','2','3'])

data = {'a': [11,44,77], 'b': [22,55,88], 'c': [33,66,99]}
frame = pd.DataFrame(data, index=['1','2','3'])

"""
    a   b   c
1  11  22  33
2  44  55  66
3  77  88  99
"""
```

2.选择标签进行索引  

```python
# 定义数据
data = {'a': [11,44,77], 'b': [22,55,88], 'c': [33,66,99]}
frame = pd.DataFrame(data, index=['1','2','3'])

# 取出某一列
print(frame['a'])
"""
1    11
2    44
3    77
Name: a, dtype: int64
"""

# 取出多列
print(frame[['a', 'c']])
"""
    a   c
1  11  33
2  44  66
3  77  99
"""

# 取出某一行（使用loc属性）
print(frame.loc['1'])
"""
a    11
b    22
c    33
Name: 1, dtype: int64
"""
```

3.数据保存与读取  

注意：如果在读取数据时，想把unnamed一列取出，则要设置index_col=0  

```python
# 定义数据
data = {'a': [11,44,77], 'b': [22,55,88], 'c': [33,66,99]}
frame = pd.DataFrame(data, index=['1','2','3'])

# 存储数据
frame.to_csv(f'test.csv')

# 读取数据方法1
dat = pd.read_csv(f"test.csv")
print(dat)
"""
   Unnamed: 0   a   b   c
0           1  11  22  33
1           2  44  55  66
2           3  77  88  99
"""

# 读取数据方法2
dat = pd.read_csv(f"test.csv", index_col=0)
print(dat)
"""
    a   b   c
1  11  22  33
2  44  55  66
3  77  88  99
"""
```
