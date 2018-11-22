#天天向上进阶版3.0.py
import math
def dayup(df):
	dayup=1.0
	for i in range(365):
		if i % 7 in [6,0]:
			dayup=dayup*(1-0.01)
		else:
			dayup=dayup*(1+df)
	return dayup

dayfactor=0.01
if (dayup(dayfactor)<37):
	dayfactor+=0.001

print(dayfactor)