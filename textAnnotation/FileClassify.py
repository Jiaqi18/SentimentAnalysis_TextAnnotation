#!/usr/bin/python
import re
filename = open('data/weibo_senti_100k.csv', 'r',encoding="utf-8")
f1 = open('potdata/weibo_senti_pos.txt','w',encoding="utf-8")
f2 = open('potdata/weibo_senti_neg.txt','w',encoding="utf-8")
#f3 = open('potdata/comment_neu.txt','w',encoding="utf-8")
lines = filename.readlines()
num  = 1
for line in lines:
    num = num + 1
    # print(line)
    """
    if line.endswith("neu\n"):
        # print(line)
        f3.write(line)
    elif line.endswith("neg\n"):
        f2.write(line)
    elif line.endswith("pos\n"):
        f1.write(line)
    
    """
    if line.startswith("0,"):
        # print(line)
        f2.write(line)
    elif line.startswith("1,"):
        f1.write(line)

print("共读取了" + str(num) + "行数据")
f1.close()
f2.close()

