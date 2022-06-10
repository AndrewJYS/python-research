def f1(arg1: str, arg2: str, arg3: str):
    print(arg1, arg2, arg3)

from itertools import product
argname = ['arg1', 'arg2', 'arg3']
arg1 = ['a1_1', 'a1_2']
arg2 = ['a2_1', 'a2_2']
arg3 = ['a3_1']
loop_val = [arg1, arg2, arg3]
for argval in product(*loop_val):
    f1(**dict(zip(argname, argval)))