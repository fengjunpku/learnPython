# -*- coding:utf-8 -*-
import time,sys,os,platform
def beep():
	i = 0
	while i<10:
		sys.stdout.write('\a\n')
		#print '\a'
		time.sleep(0.1)
		i += 1

if __name__ == "__main__":
	beep()
	if platform.system()=='Darwin':
		os.system('say "your program has finished"')
