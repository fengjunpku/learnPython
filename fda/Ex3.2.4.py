#python27
import math
from numpy import *
import matplotlib.pyplot as plt
from time import time

random.seed(30000)
t0 = time()
#parameters
S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2
M = 50
dt = T/M
I = 250000
# simu I path
S = S0*exp(cumsum((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*random.standard_normal((M+1,I)),axis=0))

S[0]=S0
C0 = math.exp(-r*T)*sum(maximum(S[-1]-K,0))/I
tnp2 = time()-t0
#print C0
#print tnp2
plt.plot(S[:,:5])
plt.show()
