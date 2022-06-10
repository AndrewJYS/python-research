# function  

## 批量调用函数  

假设有函数f1()  

```python
def f1(arg1: str, arg2: str, arg3: str):
    print(arg1, arg2, arg3)
```

而f1()每个参数又有不同的选项，如果想遍历这些参数的组合，批量调用函数f1()，可以用下面这种方式，排列组合参数，再用字典的方式传入参数  

```python
from itertools import product
argname = ['arg1', 'arg2', 'arg3']
arg1 = ['a1_1', 'a1_2']
arg2 = ['a2_1', 'a2_2']
arg3 = ['a3_1']
loop_val = [arg1, arg2, arg3]
for argval in product(*loop_val):
    f1(**dict(zip(argname, argval)))
```

输出如下：  

```python
a1_1 a2_1 a3_1
a1_1 a2_2 a3_1
a1_2 a2_1 a3_1
a1_2 a2_2 a3_1
```