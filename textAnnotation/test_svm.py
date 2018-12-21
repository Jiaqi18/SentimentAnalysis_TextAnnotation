import datetime
from multiprocessing import Process

from spa.feature_extraction import ChiSquare
from spa.tools import get_accuracy
from spa.tools import Write2File
from sklearn.externals import joblib
import time
class Test:
    def __init__(self, type_, train_num, test_num,feature_num, max_iter, C, k, corpus):
        self.type = type_
        self.train_num = train_num
        self.test_num = test_num
        self.feature_num = feature_num
        self.max_iter = max_iter
        self.C = C
        self.k = k
        self.parameters = [train_num, test_num, feature_num]
        #self.predict_num = predict_num
        # get the f_corpus
        self.train_data, self.train_labels = corpus.get_train_corpus(train_num)
        self.test_data, self.test_labels = corpus.get_test_corpus(test_num)
        # 获得预测语料
        #self.predict_data = corpus.get_predict_corpus(predict_num)
        # feature extraction
        fe = ChiSquare(self.train_data, self.train_labels)
        self.best_words = fe.best_words(feature_num)

        self.single_classifiers_got = False

        self.precisions = [[0, 0],  # bayes
                           [0, 0],  # maxent
                           [0, 0]]  # svm

    def set_precisions(self, precisions):
        self.precisions = precisions



    def write(self, filepath, classify_labels, i=-1):
        results = get_accuracy(self.test_labels, classify_labels, self.parameters)
        if i >= 0:
            self.precisions[i][0] = results[10][1] / 100
            self.precisions[i][1] = results[7][1] / 100

        Write2File.write_contents(filepath, results)

    def test_svm(self):
        print("SVMClassifier")
        print("---" * 45)
        print("Train num = %s" % self.train_num)
        print("Test num = %s" % self.test_num)
        print("C = %s" % self.C)

        from textAnnotation.SVMmodel import SVMClassifier
        svm = SVMClassifier(self.train_data, self.train_labels, self.best_words, self.C)

        classify_labels = []
        print("SVMClassifier is testing ...")
        for data in self.test_data:
            classify_labels.append(svm.classify(data))
        print("SVMClassifier tests over.")

        filepath = "model_runout/SVM-%s-train-%d-test-%d-f-%d-C-%d-%s-lin.xls" % \
                   (self.type,
                    self.train_num, self.test_num,
                    self.feature_num, self.C,
                    datetime.datetime.now().strftime(
                        "%Y-%m-%d-%H-%M-%S"))

        self.write(filepath, classify_labels, 2)

        
        print("SVMClassifier is predicting ...")
        predict_labels = []
        all_predictdoc_list = []
        filepredict = open("data\\EL_comment_fenci.txt",'r',encoding="utf8")
        filepredictResult = open("data\\Svm_result2.txt",'w',encoding="utf8")
        for line in filepredict:
            line = ''.join(line)
            all_predictdoc_list.append(line[0:])
        print("预测文本的长度为"+str(len(all_predictdoc_list)))
        predict_data = all_predictdoc_list[0:]
        for data in predict_data:
            predict_labels.append(svm.classify(data))
        print(len(predict_labels))
        """
        for label in predict_labels:
            print(label)
        """
        """
        n = 1
        line_num = 1
        while n < len(predict_labels):
            while line_num < len(filepredict.readlines()):
                line = filepredict.readline()
                print(str(predict_labels[n]))
                print(line)
                print("\r\n")
                filepredictResult.write(str(predict_labels[n]))
                filepredictResult.write(line)
                filepredictResult.write("\r\n")
                n = n + 1
                line_num = line_num + 1
        """
        n = 1
        while n < len(predict_labels):
                print(str(predict_labels[n]))
                print("\r\n")
                filepredictResult.write(str(predict_labels[n]))
                filepredictResult.write("\r\n")
                n = n + 1
        print("SVMClassifier predicting over.")

def test_weibo():
    from textAnnotation.test_svmCorpus import WeiboCorpus

    type_ = "weibo"
    train_num = 3000
    test_num = 1000
    feature_num = 5000
    max_iter = 500
    C = 150
    k = 13
    k = [1, 3, 5, 7, 9, 11, 13]
    corpus = WeiboCorpus()

    test = Test(type_, train_num, test_num, feature_num, max_iter, C, k, corpus)
    test.test_svm()



if __name__ == "__main__":
    test_weibo()




