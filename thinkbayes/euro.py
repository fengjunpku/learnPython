#* coding=utf-8*
# python27

from thinkbayes import Suite
import matplotlib.pyplot as plt

class Euro(Suite):
	def Likelihood(self,data,hypo):
		x = hypo
		if data == 'H':
			return x/100.0
		else:
			return 1-x/100.0

if __name__=="__main__":
	sample = Euro(xrange(0,101))
	dataset = 'H'*140+'T'*110
	
	for data in dataset:
		sample.Update(data)

	x = []
	y = []
	for hypo,prob in sample.Items():
		x.append(hypo)
		y.append(prob)
	plt.plot(x,y)
	plt.show()
