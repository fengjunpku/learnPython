#*coding=utf-8*
#py27
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame

dates = pd.date_range('20150101',periods=5)
df = DataFrame(
		np.random.randn(5,4),
		index = dates,
		columns = list('ABCD')
		)
