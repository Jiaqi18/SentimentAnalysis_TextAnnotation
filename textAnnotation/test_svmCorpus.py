import os
import re
import csv

class Corpus:
    def __init__(self, filepath):
        root_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.normpath(os.path.join(root_path, filepath))

        #re_split = re.compile("\s+")

        self.pos_doc_list = []
        self.neg_doc_list = []
        with open(filepath, encoding="utf-8") as f:
            """
            for line_old in csv.reader(f):
                #print(line_old)
                line = ' '.join(line_old)
                #print(line)
                #print(type(line))
                splits = re_split.split(line.strip(' '))
                #print(splits[0])
                #print(splits[1])
                if splits[0] == "1":
                    self.pos_doc_list.append(''.join(splits[1:]))
                elif splits[0] == "0":
                    self.neg_doc_list.append(splits[1:])
                    #print(splits[1:])
                else:
                    raise ValueError("Corpus Error")
            """
            for line in f.readlines():
                #print(type(line))
                #print(line)
                line = ''.join(line)
                #print(line)
                splits = line.strip(" ")
                #print(splits[0])
                #print(splits[1:])
                if line[0] == "1":
                    self.pos_doc_list.append(line[1:])
                elif line[0] == "0":
                    self.neg_doc_list.append(line[1:])
                else:
                    raise ValueError("Corpus Error")



        self.doc_length = len(self.pos_doc_list)
        print(len(self.pos_doc_list))
        print(len(self.neg_doc_list))
        # assert len(self.neg_doc_list) == self.doc_length

        self.train_num = 0
        self.test_num = 0

        runout_content = "You are using the corpus: %s.\n" % filepath
        runout_content += "There are total %d positive and %d negative f_corpus." % \
                          (self.doc_length, self.doc_length)
        print(runout_content)

    def get_corpus(self, start=0, end=-1):
        assert self.doc_length >= self.test_num + self.train_num

        if end == -1:
            end = self.doc_length

        data = self.pos_doc_list[start:end] + self.neg_doc_list[start:end]
        data_labels = [1] * (end - start) + [0] * (end - start)
        return data, data_labels

    def get_train_corpus(self, num):
        self.train_num = num
        return self.get_corpus(end=num)

    def get_test_corpus(self, num):
        self.test_num = num
        return self.get_corpus(start=self.train_num, end=self.train_num + num)

    def get_all_corpus(self):
        data = self.pos_doc_list[:] + self.neg_doc_list[:]
        data_labels = [1] * self.doc_length + [0] * self.doc_length
        return data, data_labels

    # 获得预测语料
    def get_predict_corpus(self, num):
        self.predict_num = num
        return self.get_corpus(end=num)


class WeiboCorpus(Corpus):
    def __init__(self):
        Corpus.__init__(self, "data/weibo_newnewTrainData.txt")



