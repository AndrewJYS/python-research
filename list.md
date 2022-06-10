# list

## 将列表中的每个元素转换类型  

将列表中的每个元素转换类型，可能在pandas的DataFrame中有用。例如要生成列表['1', '3', '5', '7', '9']，则可以用下述语句，先生成int元素的列表，再做转换  

```python
a = list(map(str, list(range(1, 10, 2))))
```

逐步打印结果如下：

```python
a = list(range(1, 10, 2))
b = map(str, a)
c = list(b)
print(a, b, c, sep='\n')

# 输出
[1, 3, 5, 7, 9]
<map object at 0x00000193D15CB3A0>
['1', '3', '5', '7', '9']
```
