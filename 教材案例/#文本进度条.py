#文本进度条.py
import time
scale=10
print("-----执行开始-----")
for i in range(scale+1):
	a,b='**' * i,'..'*(i-1)
	c=(i/scale)*100
	print("%{:^3.0f}[{}->{}]".format(c,a,b))
	time.sleep(1)
print("-----执行结束-----")	