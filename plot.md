# plot  

## 给函数传递matplotlib对象  

如果要绘制一个大图，其中包含了多个子图，每个子图的数据处理过程相似，由一组参数控制，那么可以将子图的数据处理和绘制任务封装成函数，每画一个子图，则向函数传递数据处理的参数和初始化的子图(matplotlib)对象，整体的结构如下：  

```python
import matplotlib.pyplot as plt

def subplt(ax:'plt_obj', **kwargs):
    # 利用kwargs参数处理数据
    # 处理完后将这些数据绘制到ax对象上

def run():
    fig, axes = plt.subplots(3, 4)
    for ax in axes:
        subplt(ax, ...)
    ...
```
