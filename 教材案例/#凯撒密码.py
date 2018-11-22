#凯撒密码.py
plaincode=input("输入密码：")
for i in plaincode:
	if ord("a") <= ord(i) <=ord("z"):
		print(chr(ord("a")+(ord(i)-ord("a")+3)%26),end='')
	else:
		print(i,end='')