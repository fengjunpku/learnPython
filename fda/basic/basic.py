#*coding=utf-8*
#py27
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

norm = stats.norm(loc=0.5,scale=2)
data = norm.rvs(size=20000)

mu = np.mean(data)
sigma = np.std(data)
stat_val, p_val = stats.kstest(data, 'norm', (mu, sigma))
print 'KS-statistic D = %6.3f p-value = %6.4f' % (stat_val, p_val)

stat_val, p_val = stats.ttest_1samp(data,0.5)
print 'one-sample t-statistic D = %6.3f p-value = %6.4f' % (stat_val, p_val)
