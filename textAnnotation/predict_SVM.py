from sklearn.svm import SVC
from sklearn.externals import joblib
from textAnnotation.SVMmodel import SVMClassifier
import numpy as np
from spa.feature_extraction import ChiSquare
from textAnnotation.test_svmCorpus import WeiboCorpus
def words2vector( all_data):
    vectors = []
    corpus = WeiboCorpus()
    train_data, train_labels = corpus.get_train_corpus(3000)
    fe = ChiSquare(train_data, train_labels)
    best_words = fe.best_words(5000)
    best_words_index = {}
    for i, word in enumerate(best_words):
        best_words_index[word] = i

    for data in all_data:
        vector = [0 for x in range(len(best_words))]
        for word in data:
            i = best_words_index.get(word)
            if i is not None:
                vector[i] = vector[i] + 1
        vectors.append(vector)

    vectors = np.array(vectors)
    return vectors


if __name__ == "__main__":


    # 读取模型
    model = joblib.load("model\weibo_svmModel.joblib_061953")
    #model.predict()
    #print(svm)
    # 加载方法
    #clf = SVC(C=150)
    print("SVMClassifier is predicting ...")
    predict_labels = []
    all_predictdoc_list = []
    filepredict = open("data\\EL_comment_fenci.txt",'r',encoding="utf8")
    filepredictResult = open("data\\Svm_comment_result.txt",'w',encoding="utf8")
    for line in filepredict:
        line = ''.join(line)
        all_predictdoc_list.append(line[0:])
    print("预测文本的长度为"+str(len(all_predictdoc_list)))
    predict_data = all_predictdoc_list[0:]
    for data in predict_data:
        vector = words2vector([data])
        predict_labels.append((model.predict(vector))[0])
    """
    for label in predict_labels:
        filepredictResult.write(label)
        filepredictResult.write("\r\n")
    """
    n = 1
    line_num = 1
    while n < len(predict_labels):
        while line_num < len(filepredict.readlines()):
            line = filepredict.readline()
            filepredictResult.write(str(predict_labels[n]))
            filepredictResult.write(line)
            filepredictResult.write("\r\n")
            n = n + 1
            line_num = line_num + 1
    print("SVMClassifier predicting over.")