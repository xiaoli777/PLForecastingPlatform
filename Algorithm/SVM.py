"""
第四代：仅对未来进行预测，使用未来数据，不使用预测数据,对一些异常点单独测试，模块化，SVM预测模型
"""
import pymysql
import numpy as np
import datetime
import math
from sklearn import svm
import warnings

name = "支持向量机"
Threshold = 30  # 30 10 10
sigma = math.sqrt(0.5)  # 0.5 1 0.5
mu = 0.94  # 0.94 0.925 0.945
gamma = 0.126  # 0.126 0.126 0.126
SIM_range = 0  # 0 1 1


class PredictList:
    def __init__(self, date=[], real=[], predict=[], MAPE=0):
        self.date = date
        self.real = real
        self.predict = predict
        self.MAPE = MAPE


def data_search(searchtype, dd, ss, hld, fs, type=1, datatype=1):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()
    TempList = []
    Count = cur.execute('select ' + searchtype + ' from data' + dd + ss + hld + fs)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        TempList.append(('%s' % r))
    if type == 1:
        if Count > Threshold:
            Temp = TempList[Count - Threshold:]
        else:
            Temp = TempList
    else:
        Temp = TempList
    cur.scroll(0, mode='absolute')
    cur.close()
    conn.close()
    if datatype == 1:
        TempList = []
        for num in Temp:
            num = float(num)
            TempList.append(num)
        return TempList
    else:
        cur.scroll(0, mode='absolute')
        return Temp


def CalDays(date_1, date_2):
    time_1 = datetime.datetime.strptime(date_1, '%Y-%m-%d')
    time_2 = datetime.datetime.strptime(date_2, '%Y-%m-%d')
    result = (time_2 - time_1).days
    return result


def CalMAPE(Data_List_1, Data_List_2):
    SumMAPE = 0
    for pl in range(len(Data_List_1)):
        SumMAPE += abs(Data_List_1[pl] - Data_List_2[pl]) / Data_List_1[pl]
    MAPE = SumMAPE / len(Data_List_1)
    return MAPE


def Predict_Main(date_start="2007-1-1", date_end="2007-1-7", predict_type=1, paramter= 3):
    warnings.filterwarnings("ignore")

    date_predict = []
    SVM_result = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    if predict_type:
        Count = cur.execute('select date from data where date >= "'
                            + date_start + '" and date <= "' + date_end + '";')
        if Count == 0:
            print("数据库中无数据！")
        results = cur.fetchall()
        result = list(results)
        for r in result:
            date_predict.append(('%s' % r))
        date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"
    else:
        Count = cur.execute('select date from data where date = "' + date_start + '";')
        if Count == 0:
            print("数据库中无此数据！")
        results = cur.fetchall()
        result = list(results)
        for r in result:
            date_predict.append(('%s' % r))
        date_during = " where date = '" + date_start + "'"
    cur.scroll(0, mode='absolute')

    AverTemper_predict = data_search("AverTemper", date_during, "", "", ";", 0, 1)
    AverPress_predict = data_search("AverPress", date_during, "", "", ";", 0, 1)
    AverSPress_predict = data_search("AverSPress", date_during, "", "", ";", 0, 1)
    LowTemper_predict = data_search("LowTemper", date_during, "", "", ";", 0, 1)
    HighTemper_predict = data_search("HighTemper", date_during, "", "", ";", 0, 1)
    LowPress_predict = data_search("LowPress", date_during, "", "", ";", 0, 1)
    HighPress_predict = data_search("HighPress", date_during, "", "", ";", 0, 1)
    PowerLoadMax_real = data_search("PowerLoadMax", date_during, "", "", ";", 0, 1)

    cur.close()
    conn.close()

    for date_index in range(len(date_predict)):
        date_during = " where date < '" + date_predict[date_index] + "'"
        season = " and date in (select date from date where season = (select season from date where date = '" + date_predict[date_index] + "'))"
        holiday = " and date in (select date from date where holiday = (select holiday from date where date = '" + date_predict[date_index] + "'))"
        finish_signal = ";"

        if paramter == 1:
            season = ""
            holiday = ""
        elif paramter == 3:
            holiday = ""
        elif paramter == 5:
            season = ""
        else:
            pass

        data_history = data_search("date", date_during, season, holiday, finish_signal, 1, 0) \
                       + [date_predict[date_index], ]
        AverTemper = data_search("AverTemper", date_during, season, holiday, finish_signal, 1, 1) \
                     + [AverTemper_predict[date_index], ]
        AverPress = data_search("AverPress", date_during, season, holiday, finish_signal, 1, 1) \
                    + [AverPress_predict[date_index], ]
        AverSPress = data_search("AverSPress", date_during, season, holiday, finish_signal, 1, 1) \
                     + [AverSPress_predict[date_index], ]
        LowTemper = data_search("LowTemper", date_during, season, holiday, finish_signal, 1, 1) \
                    + [LowTemper_predict[date_index], ]
        HighTemper = data_search("HighTemper", date_during, season, holiday, finish_signal, 1, 1) \
                     + [HighTemper_predict[date_index], ]
        LowPress = data_search("LowPress", date_during, season, holiday, finish_signal, 1, 1) \
                   + [LowPress_predict[date_index], ]
        HighPress = data_search("HighPress", date_during, season, holiday, finish_signal, 1, 1) \
                    + [HighPress_predict[date_index], ]
        PowerLoadMax = data_search("PowerLoadMax", date_during, season, holiday, finish_signal, 1, 1)
        
        #print(data_history)
        current_data = []
        current_data.append(AverTemper_predict[date_index])
        current_data.append(AverPress_predict[date_index])
        current_data.append(AverSPress_predict[date_index])
        current_data.append(LowTemper_predict[date_index])
        current_data.append(HighTemper_predict[date_index])
        current_data.append(LowPress_predict[date_index])
        current_data.append(HighPress_predict[date_index])

        samplein = np.mat([AverTemper, AverPress, AverSPress, LowTemper, HighTemper, LowPress, HighPress])
        sample_predict = np.mat([current_data, ] * len(data_history)).T
        sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0], samplein.max(axis=1).T.tolist()[0]]).transpose()
        sampleinnorm = ((np.array(samplein.T) - sampleinminmax.transpose()[0]) / (
        sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()
        sample_predictnorm = ((np.array(sample_predict.T) - sampleinminmax.transpose()[0]) / (
        sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()

        sample_temp = sampleinnorm - sample_predictnorm
        SIMMartrix = np.zeros([sample_temp.shape[0], sample_temp.shape[1]])
        SIMCount = [0, ] * sample_temp.shape[1]

        for row in range(sample_temp.shape[0]):
            for column in range(sample_temp.shape[1]):
                if np.exp(-(sample_temp[row][column] ** 2) / (2 * sigma * sigma)) >= mu:
                    SIMMartrix[row][column] = 1
                    SIMCount[column] += 1
                else:
                    SIMMartrix[row][column] = 0

        SIMCount.pop()
        SVM_X = []
        SVM_y = []
        MaxIndexCount = 0
        for i in range(len(SIMCount)):
            if SIMCount[i] >= (max(SIMCount) - SIM_range):
                MaxIndexCount += 1
                SVM_X.append([AverTemper[i], AverPress[i], AverSPress[i], LowTemper[i], HighTemper[i], LowPress[i],
                              HighPress[i]])
                SVM_y.append(PowerLoadMax[i])

        clf = svm.SVR()
        clf.fit(SVM_X, SVM_y)
        predict_result = round(float(clf.predict(current_data)), 2)
        SVM_result.append(predict_result)

    DateAmend = []
    index = 0
    for da in date_predict:
        if len(date_predict) >= 10:
            if (index) % (int(len(date_predict) / 10)) == 0:
                da = da[5:]
            else:
                da = ""
            index = index + 1
        else:
            da = da[5:]
        DateAmend.append(da)

    # 计算MAPE
    MAPE = CalMAPE(PowerLoadMax_real, SVM_result)
    return PredictList(DateAmend, PowerLoadMax_real, SVM_result, MAPE)


if __name__ == '__main__':
    Result = Predict_Main()
    print(Result.date)
    print(Result.real)
    print(Result.predict)
