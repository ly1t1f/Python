#jieba常用知识点
#jieba常用的分词函数
#jieba.cut(s)  精确模式，返回一个可迭代的数据类型
#jieba.cut(s，cut_all=True)  全模式，返回文本s中所有可能的单词
#jieba.cut_for_search(s)	搜索引擎模式，适合搜索引擎建立索引的分词结果
#jieba.lcut(s)	精确模式，返回一个列表类型
#jieba.lcut(s,cut_all=True)		全模式，返回一个列表类型
#jieba.lcut_for_search(s)	搜索引擎模式，返回一个列表类型
#jieba.add_word(w)		向分词词典中增加新词w

import jieba
a=jieba.lcut("中华人民共和国是一个伟大的国家")
b=jieba.lcut("中华人民共和国是一个伟大的国家",cut_all=True)
c=jieba.lcut_for_search("中华人民共和国是一个伟大的国家")
d=jieba.lcut("习大大期盼有更好的教育")
jieba.add_word("习大大")
e=jieba.lcut("习大大期盼有更好的教育")

print(a,b,c,d,e,end='\n')