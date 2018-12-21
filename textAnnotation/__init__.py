# from textAnnotation.DictModel import DictClassifier
from textAnnotation.SVMmodel import SVMClassifier
import jieba
import pandas as pd

import numpy as np
if __name__ == '__main__':
    # 基于词典的方法进行文本分类，结果保存在potdata中
    # d = DictClassifier()
    # result = d.analysis_file(filepath_in="data/answer_comments_2.txt",filepath_out="data/comment_potresult.txt")
    # 2018.11.30尝试用SVM文本分类，有监督的机器学习方法，微博语料的加载已经完成
    # 119988微博语料，正向59993，负向59995
    """
    path = 'data/'
    pd_all = pd.read_csv(path + 'weibo_senti_100k.csv')
    # print(pd_all)
    #f = open("data\weibo_trainData.txt",'w',encoding='utf-8')
    print('评论数目（总体）：%d' % pd_all.shape[0])
    print('评论数目（正向）：%d' % pd_all[pd_all.label == 1].shape[0])
    print('评论数目（负向）：%d' % pd_all[pd_all.label == 0].shape[0])
    # train_data = []
    train_data = np.array(pd_all['review'])
    train_label = np.array(pd_all['label'])
    
    """

    """
    # 将train_data写入txt文件，方便分词处理
    for i in list(train_data):
        #print(i)
        f.write(str(i))
        f.write("\r\n")

    """
    """
    # 将分词后的微博语句和对应的标签重新组合在一起
    f1 = open("data\weibo_newTrainData.txt",'w',encoding='utf-8')
    f2 = open("data\weibo_fenci.txt",'r',encoding='utf-8')
    label_len = len(train_label)
    #print(label_len)
    n = 1
    line_num = 1
    while n < label_len:
        while line_num < 119986:
            line = f2.readline()
            f1.write(str(train_label[n]))
            f1.write(line)
            f1.write("\r\n")
            n = n + 1
            line_num = line_num + 1
    print(train_data)
    print(train_label)
    """
    """
    # 对生成的txt文件去空行
    f1 = open("data\\Svm_result2.txt", 'r', encoding='utf-8')
    f3 = open("data\\Svm_result_label.txt", 'w', encoding='utf-8')
    for line in f1.readlines():
        if line != '\n':
            f3.write(line)
    """





    """
    # 俩个txt文件合成一个，一行一行的对应
    file1 = open("data\\EL_comment_fenci.txt", 'r', encoding="utf8")
    file2 = open("data\\Svm_result_label.txt", 'r', encoding="utf8")
    file3 = open("data\\Svm_result111.txt", 'w', encoding="utf8")
    n = 0
    line_num = 0
    list1 = []
    list2 = []
    for line in file2.readlines():
        #print(line)
        list1.append(line)
    for line in file1.readlines():
        #print(line)
        list2.append(line)
    while n < len(list1):
        while line_num < len(list2):
            line1 = str(list1[n]).replace('\n', ' ')
            line2 = list2[line_num]
            file3.write(line1)
            file3.write(line2)
            file3.write("\r\n")
            line_num = line_num + 1
        n = n + 1
    print(len(list1))
    print(len(list2))



    """
