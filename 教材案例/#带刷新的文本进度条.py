#带刷新的文本进度条.py
import time
scale=50
t=time.clock()
print("程序开始".center(scale//2,'-'))
for i in range(scale+1):
	a='*'*i;
	b='.'*(scale-i)
	c=(i/scale)*100
	t-=time.clock()
	#time.clock()第一次出现表示计时开始
	#第二次出现返回与第一次出现的时间差
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),\
		end='')

	time.sleep(0.1)

print("\n"+"程序结束".center(scale//2,'-'))
