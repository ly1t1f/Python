def into_Csv(): # 导入csv格式数据到列表
    fo = open("D:\Desktop\python小练习\python——revive\教材案例\\price2016.csv","r")
    ls=[]
    for line in fo:
        line = line.replace("\n","")
        ls.append(line.split(","))
    print(ls)
    fo.close()

def del_co():#去掉逗号
    fo = open("D:\Desktop\python小练习\python——revive\教材案例\\price2016.csv", "r")
    ls = []
    for line in fo:
        line = line.replace("\n", "")
        ls=line.split(",")
        lns=""
        for s in  ls:
            lns+="{}\t".format(s)
        print(lns)
    fo.close()

def write_Csv(): #将一位数据写入.csv
    fo = open("D:\Desktop\python小练习\python——revive\教材案例\\price2016.csv", "w")
    ls = ['北京','101.5','120.7','121.4']
    fo.write(",".join(ls)+"\n")
    fo.close()

def write_T():#将二维数据写入csv
    fr = open("D:\Desktop\python小练习\python——revive\教材案例\\price2016.csv", "r")
    fw = open("D:\Desktop\python小练习\python——revive\教材案例\\price2016_Out.csv", "w")
    ls=[]
    for line in fr:# 将csv中的二维数据读入到列表变量
        line = line.replace("\n","")
        ls.append(line.split(","))
    for i in range(len(ls)):#遍历列表计算百分数
        for j in range(len(ls[i])):
            if ls[i][j].replace("."",","").isnumeric():
                ls[i][j]="{:.2}%".format(float(ls[i][j])/100)
    for row in ls:#将列表变量中的两位数据输出到csv文件中
        print(row)
        fw.write(",".join(row)+"\n")
    fr.close()
    fw.close()


if __name__ == "__main__":
    # into_Csv()
    # del_co()
    # write_Csv()
    write_T()