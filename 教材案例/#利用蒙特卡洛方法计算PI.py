#利用蒙特卡洛方法计算PI
import time
import random
import math

darts=1000
#darts表示抛点数.py
hits=0.0
time.clock()
for i in range(1,darts+1):
	x,y=random.random(),random.random()
	#为x，y赋值两个随机浮点数
	dist=math.sqrt(x**2+y**2)
	# x**2表示x的2次幂
	if dist<=1.0:
		hits+=1

pi=4*(hits/darts)
print("PI的值是{}".format(pi))
print("runtime:{}".format(time.clock()))
	
