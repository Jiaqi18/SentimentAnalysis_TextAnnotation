from sklearn.svm import SVC
import numpy as np
import datetime
from sklearn.externals import joblib
import time

class SVMClassifier:
    def __init__(self, train_data, train_labels, best_words, C):
        train_data = np.array(train_data)
        print(train_data.shape)
        train_labels = np.array(train_labels)

        self.best_words = best_words
        self.clf = SVC(C=C)
        self.__train(train_data, train_labels)

    def words2vector(self, all_data):
        vectors = []

        best_words_index = {}
        for i, word in enumerate(self.best_words):
            best_words_index[word] = i

        for data in all_data:
            vector = [0 for x in range(len(self.best_words))]
            for word in data:
                i = best_words_index.get(word)
                if i is not None:
                    vector[i] = vector[i] + 1
            vectors.append(vector)

        vectors = np.array(vectors)
        return vectors



    def trainSVM(self, train_data, train_labels):
        print("SVMClassifier is training ...... ")

        train_vectors = self.words2vector(train_data)

        self.clf.fit(train_vectors, np.array(train_labels))

        print("SVMClassifier trains over!")


    def __train(self, train_data, train_labels):
        print("SVMClassifier is training ...... ")

        train_vectors = self.words2vector(train_data)

        self.clf.fit(train_vectors, np.array(train_labels))
        # 给保存的模型的名字加上时间标签，以区分训练过程中产生的不同的模型
        mdhms = time.strftime('%d%H%M', time.localtime(time.time()))
        # 保存的模型的文件名
        file = r'model\weibo_svmModel.joblib' + '_' + mdhms
        # 保存模型
        joblib.dump(self.clf, file)
        print("SVMClassifier trains over!")

    def classify(self, data):
        vector = self.words2vector([data])

        prediction = self.clf.predict(vector)

        return prediction[0]

