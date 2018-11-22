#求平均值，标准差和中位数.py
import math

def getNum():
	nums=[]
	num=input("请输入数字： ")
	while num !="":
		nums.append(eval(num))
		num=input("请输入数字： ")
	return nums

def avg(n):
	sum=0
	
	for i in n:
		sum=sum+i
	return sum/len(n)

def med(n):
	medi=0
	sorted(n)
	if len(n)%2!=0:
		medi=n[(len(n)+1)//2]
	else:
		medi=n[(len(n)+2)//2]

	return medi

def sdev(n,m):
	s=0.0
	for i in n:
		s=s+(i-m)**2

	return math.sqrt(s/(len(n)-1))

n=getNum()
m=med(n)
print("平均值：{}，平均数：{}，方差：{:.2}".format(m,med(n),sdev(n,m)))
print(n)