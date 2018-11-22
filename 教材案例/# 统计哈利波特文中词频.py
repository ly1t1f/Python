# 统计哈利波特文中词频.py
import jieba
# excludes排除不想要的单词
excludes={"the","and","of","a"}
def getText():
	txt = open("D:\Desktop\python小练习\python——revive\教材案例\hali.txt","r").read()
	txt=txt.lower()
	for ch in '!"#$%*()&@~<>+=-':
		txt=txt.replace(ch," ")
	return txt

hamTxt=getText()
words=hamTxt.split() # 将单词分隔开
counts={}
for word in words:
	counts[word]=counts.get(word,0)+1

for word in excludes:
	del(counts[word])

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
	word,count=items[i]
	print("{0:<10}{1:<5}".format(word,count))
