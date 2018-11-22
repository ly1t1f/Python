#字符串反转.py
def reverse(s):
	if s=="":
		return s
	else:
		return reverse(s[1:])+s[0]
s=input("输入字符串：")
print(reverse(s))