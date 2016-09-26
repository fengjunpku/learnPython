#*coding=utf-8*
#py27
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

d = {'one':[1,2,3,4],'two':[7,9,4,8],'three':[10,23,8,12]}
df =DataFrame(d, index=['a','b','c','d'])
print df
print '########'
print df[['one','two']]
print '########'
print df.loc['a']
print df.iloc[1]
print df['one']
print '########'
print df[1:4]
