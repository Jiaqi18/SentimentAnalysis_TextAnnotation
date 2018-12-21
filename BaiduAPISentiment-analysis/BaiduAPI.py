from aip import AipNlp
import csv
import pandas as pd
from pandas.core.frame import DataFrame
import json
# encoding = "utf-8"
""" 你的 APPID AK SK """
# 利用百度云提供的API接口实现情感分析
APP_ID = '15032766'
API_KEY = '4TxaOcg2audetMg88uTqEoNe'
SECRET_KEY = 'q02GOFLOfSd9yYX8ALCBbxypf4xjvY1x'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 写入文件
def output():
    urls = []
    with open('E:\comment_data\\answer_comments_2.txt','r',encoding="utf8" ,errors='ignore') as f:

        for row in f.readlines():
            urls.append(row)
    return urls

# 对读入的数据进行情感分析，将其得到的结果解析成标准JSON格式数据，并保存在一个新的dict中
def sentimentClassify():
    x = output()
    i=1
    tt= []
    pp=[]
    np=[]
    con=[]
    sen=[]
    all={}
    for i in range(len(x)):
        #text = json.dumps(x[i]).encode('utf-8')
        text=x[i]
        # 通过百度提供的接口方法进行情感倾向提取
        try:
            result=client.sentimentClassify(text);
        except Exception:
            continue

        #print(result)
        # 如果解析错误则填写上空值,使得程序不会出错而停止运行
        if "error_code" in result.keys():
            tt.append(" ")
            pp.append(" ")
            np.append(" ")
            con.append(" ")
            sen.append(" ")
            all["text"] = tt
            all["positive_prob"] = pp
            all["negative_prob"] = np
            all["confidence"] = con
            all["sentiment"] = sen
        else:
            data = result['items']
            items = data[0]
            text = result['text']
            tt.append(text)
            positive_prob = items['positive_prob']
            pp.append(positive_prob)
            negative_prob = items['negative_prob']
            np.append(negative_prob)
            confidence = items['confidence']
            con.append(confidence)
            sentiment = items['sentiment']
            sen.append(sentiment)
            all["positive_prob"] = pp
            all["negative_prob"] = np
            all["confidence"] = con
            all["sentiment"] = sen
            all["text"] = tt
        # print(all)
    return all
    # print(all)


# 将得到的dict存储到原始的CSV文件中，方便后续进行分析
def add(ulist):
    # print(ulist)
    with open('data\\answer_comments_result.csv', 'w', newline='') as csvfile:
        headers = ['text', 'positive_prob', 'negative_prob', 'confidence','sentiment']
        writer = csv.DictWriter(csvfile, headers)
        writer.writeheader()
    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame(ulist)
    print(dataframe)
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("data\\answer_comments_result.csv", index=False, sep=',')
    """
    csv_input = open('data\\answer_comments_result.csv', 'w', newline='')
    pp = DataFrame(ulist['positive_prob'])
    csv_input["positive_prob"] = pp
    csv_input.to_csv('E:\comment_data\\answer_comments_2.csv', index=False, encoding='gbk')
    np = DataFrame(ulist['negative_prob'])
    csv_input["negative_prob"] = np
    csv_input.to_csv('E:\comment_data\\answer_comments_2.csv', index=False, encoding='gbk')
    con = DataFrame(ulist['confidence'])
    csv_input["confidence"] = con
    csv_input.to_csv('E:\comment_data\\answer_comments_2.csv', index=False, encoding='gbk')
    sen = DataFrame(ulist['sentiment'])
    csv_input["sentiment"] = sen
    csv_input.to_csv('E:\comment_data\\answer_comments_2.csv', index=False, encoding='gbk')
    """






if __name__ == '__main__':
    add(sentimentClassify())
    # add({'positive_prob': [0.484195], 'negative_prob': [0.515805], 'confidence': [0.683905], 'sentiment': [1], 'text': '求链接'})

