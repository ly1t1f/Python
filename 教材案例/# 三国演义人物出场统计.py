# 三国演义人物出场统计.py
import jieba
excludes={"将军","二人","荆州","不可","不能","如此","却说","商议"}
txt=open("D:\Desktop\python小练习\python——revive\教材案例\三国演义.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts={}
for word in words:
	if len(word)==1:
		# 排除单个字符的分词结果
		continue
	elif word=="诸葛亮" or word=="孔明曰":
		rword="孔明"

	elif word=="关公" or word=="云长":
		rword="关羽"
	elif word=="玄德" or word=="玄德曰":
		rword="刘备"
	elif word=="孟德" or word=="丞相":
		rword="曹操"
	else:
		reword=word
		counts[word]=counts.get(word,0)+1

for word in excludes:
	del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
	word,count=items[i]
	print("{0:<10}{1:<5}".format(word,count))

