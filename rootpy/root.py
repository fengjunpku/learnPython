#!/home/fengjun/bin/py27
import ROOT
# Example: displaying a ROOT histogram from Python
from ROOT import gRandom,TCanvas,TH1F
c1 = TCanvas('c1','Example',200,10,700,500)
hpx = TH1F('hpx','px',200,-10,10)
for i in xrange(25000):
	px = gRandom.Gaus(0,1)
	hpx.Fill(px)
	hpx.Draw()
	c1.Update()

