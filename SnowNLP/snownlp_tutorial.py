import sys
import pandas as pd
from snownlp import sentiment
from snownlp import SnowNLP
urls = []
f = open('E:\comment_data\\answer_comments_2.txt', 'r', encoding="utf8")
f1 = open("data\comment_data_result_snownlp","w",encoding="utf8")
# sentiment.train("data\weibo_senti_neg.txt","data\weibo_senti_pos.txt")
# sentiment.save('model\sentiment.marshal')

for row in f.readlines():
    row = row.replace("\n",' ')
    s = SnowNLP(row)
    score = s.sentiments
    if score > 0.6:
        flag = "pos"
    elif score < 0.4:
        flag = "neg"
    else:
        flag = "neu"
    row_new = []
    row_new.append(row)
    row_new.append(" ")
    row_new.append(str(score))
    row_new.append(" ")
    row_new.append(flag)
    row_new1 = ''.join(row_new)
    print(row_new1)
    f1.write(row_new1)
    f1.write("\r\n")
