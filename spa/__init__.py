from spa.classifiers import DictClassifier
import jieba
if __name__ == '__main__':
    d = DictClassifier()
    result = d.analysis_file(filepath_in="f_corpus/myhotel_test.txt",filepath_out="f_corpus/myhotel_result.txt",encoding="gbk")


