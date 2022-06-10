from scipy import stats

# loc设置均值，scale设置方差
x1 = stats.norm.rvs(loc=10, scale=2, size=100)
x2 = stats.norm.rvs(loc=10, scale=2, size=100)

res = stats.ttest_1samp(x1, [5, 10])
# print(res)
# print(res[0], res[1])

"""
输出
Ttest_1sampResult(statistic=array([24.68375977,  1.49978143]), pvalue=array([4.30106938e-44, 1.36853379e-01]))
[24.68375977  1.49978143] [4.30106938e-44 1.36853379e-01]
"""

# loc设置均值，scale设置方差
x1 = stats.norm.rvs(loc=10, scale=2, size=100)

res = stats.ttest_1samp(x1, 5)
# print(res)
# print(res[0], res[1])

"""
输出
Ttest_1sampResult(statistic=27.655846757819532, pvalue=2.286912536675081e-48)
27.655846757819532 2.286912536675081e-48
"""

# loc设置均值，scale设置方差
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

