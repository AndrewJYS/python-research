# statistics

## t-test  

### 单样本t-检验

stats.ttest_1samp  

```python
from scipy import stats

# loc设置均值，scale设置方差
x1 = stats.norm.rvs(loc=10, scale=2, size=100)

res = stats.ttest_1samp(x1, 5)
print(res)
print(res[0], res[1])

"""
输出
Ttest_1sampResult(statistic=27.655846757819532, pvalue=2.286912536675081e-48)
27.655846757819532 2.286912536675081e-48
"""
```

也可以同时检验多列数据  

```python
x1 = stats.norm.rvs(loc=10, scale=2, size=100)
x2 = stats.norm.rvs(loc=10, scale=2, size=100)

res = stats.ttest_1samp(x1, [5, 10])
print(res)
print(res[0], res[1])

"""
输出
Ttest_1sampResult(statistic=array([24.68375977,  1.49978143]), pvalue=array([4.30106938e-44, 1.36853379e-01]))
[24.68375977  1.49978143] [4.30106938e-44 1.36853379e-01]
"""
```

### 两独立样本t检验  

若不确定两样本方差是否相等时，应先用levene检验，检验两样本是否具有方差齐性。若pvalue>>0.05，则认为两样本具有方差齐性。若两样本不具有方差齐性，需要将equal_val参数设定为False。levene检验示例如下:  

```python
x1 = stats.norm.rvs(loc=10, scale=2, size=100)
x2 = stats.norm.rvs(loc=10, scale=2, size=100)
print(stats.levene(x1, x2))

# 输出
LeveneResult(statistic=0.7884931634979921, pvalue=0.3756335541071659)
```

两独立样本t检验(stats.ttest_ind)示例如下：  

```python
x1 = stats.norm.rvs(loc=10, scale=2, size=100)
x2 = stats.norm.rvs(loc=9, scale=10, size=100)

print(stats.levene(x1, x2))
res = stats.ttest_ind(x1, x2, equal_var=False)
print(res)

"""
输出
LeveneResult(statistic=107.34890694602971, pvalue=2.244677585060153e-20)
Ttest_indResult(statistic=0.35687219868851355, pvalue=0.7218894213754461)
"""
```

综上所述，可以把两独立样本t检验封装成下述函数：  

```python
def Ttest_ind(self, x1, x2):
    """
    scipy.stats ttest_ind(x1, x2), 但封装了对方差齐性的判断
    @return:
    """
    lev = stats.levene(x1, x2)
    if lev[1] > 0.05:
        ttest = stats.ttest_ind(x1, x2, equal_var=True)
    else:
        ttest = stats.ttest_ind(x1, x2, equal_var=False)
    return ttest
```
