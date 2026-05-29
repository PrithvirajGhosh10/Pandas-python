#data filteration
import pandas as pd
data=[100,102,104,200,202]
series=pd.Series(data,index=("a","b","c","d","e"))
print(series[series>=200])
'''
d    200
e    202
dtype: int64
'''
print(series[series<200])
'''
a    100
b    102
c    104
dtype: int64
'''

