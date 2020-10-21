"""
第四代：仅对未来进行预测，使用未来数据，不使用预测数据,对一些异常点单独测试，模块化，SVM预测模型
"""
import pymysql
import numpy as np
import datetime
import math
from sklearn import svm
import warnings

name = "SVM回归分析"
Threshold = 45 # 49
#sigma = math.sqrt(0.5)  # 0.5
#mu = 0.94  # 0.94
#SIM_range = 1  # 1
#sigmaList = [math.sqrt(0.5),math.sqrt(1)]
#muList = [0.7,0.8,0.9,0.94]
SIM_range = 1
#sigmaList = [math.sqrt(0.25),math.sqrt(0.5),math.sqrt(0.75),math.sqrt(1),math.sqrt(1.25),math.sqrt(1.5),math.sqrt(1.75),math.sqrt(2)]
sigmaList = [math.sqrt(0.25),math.sqrt(0.5),math.sqrt(0.75),math.sqrt(1)]
#sigmaList = [math.sqrt(0.5),math.sqrt(1)]
#muList = [0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.9,0.925,0.94,0.95,0.975,0.98,0.985,0.99]
#muList = [0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99]
#muList = [0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.9,0.91,0.925,0.94,0.95,0.96,0.975,0.98,0.99]
#muList = [0.7,0.75,0.8,0.85,0.9,0.91,0.925,0.94,0.95,0.96,0.975,0.98,0.99]
muList = [0.9,0.91,0.925,0.94,0.95,0.96,0.975,0.98,0.99]
MaxValue = 10000

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

def pre_week(date_list,predict_type,index):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()
    current_data_list = []

    for date in date_list:
        current_data = []
        Count = cur.execute('select ' + predict_type + ' from data '
                            'where date = DATE_SUB("' + date + '",'
                            'INTERVAL ' + str(index) + ' DAY);')
        if Count == 0:
            Count = cur.execute('select ' + predict_type + ' from data '
                                'where date = "' + date + '";')
        results = cur.fetchall()
        result = list(results)
        for r in result:
            current_data.append(('%s' % r))
        for num in current_data:
            num = float(num)
            current_data_list.append(num)

    cur.close()
    conn.close()
    return current_data_list

def CalMAPE(Data_List_1, Data_List_2):
    SumMAPE = 0
    for pl in range(len(Data_List_1)):
        SumMAPE += abs(Data_List_1[pl] - Data_List_2[pl]) / Data_List_1[pl]
    MAPE = SumMAPE / len(Data_List_1)
    return MAPE

def CalMASE(Data_List_1, Data_List_2):
    SumMASE_1 = 0
    SumMASE_2 = 0
    for pl in range(len(Data_List_1)):
        SumMASE_1 += abs(Data_List_2[pl] - Data_List_1[pl])
        if pl:
            SumMASE_2 += abs(Data_List_1[pl - 1] - Data_List_1[pl])
    MASE_1 = SumMASE_1 / len(Data_List_1)
    MASE_2 = SumMASE_2 / (len(Data_List_1) - 1)
    MASE = MASE_1 / MASE_2
    return MASE

def Predict_Main(date_start="2007-1-1", date_end="2007-12-31", paramter = 5, predicttype="Max"):
    warnings.filterwarnings("ignore")

    if predicttype == "Max":
        predict_type = "PowerLoadMax"
    elif predicttype == "Aver":
        predict_type = "PowerLoadAver"
    elif predicttype == "Min":
        predict_type = "PowerLoadMin"
    else:
        pass

    date_predict = []
    SVM_result = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()
    Count = cur.execute('select date from data where date >= "'
                        + date_start + '" and date <= "' + date_end + '";')
    if Count == 0:
        print("数据库中无数据！")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        date_predict.append(('%s' % r))
    date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"

    cur.scroll(0, mode='absolute')
    cur.close()
    conn.close()

    AverTemper_predict = data_search("AverTemper", date_during, "", "", ";", 0, 1)
    AverPress_predict = data_search("AverPress", date_during, "", "", ";", 0, 1)
    AverSPress_predict = data_search("AverSPress", date_during, "", "", ";", 0, 1)
    LowTemper_predict = data_search("LowTemper", date_during, "", "", ";", 0, 1)
    HighTemper_predict = data_search("HighTemper", date_during, "", "", ";", 0, 1)
    LowPress_predict = data_search("LowPress", date_during, "", "", ";", 0, 1)
    HighPress_predict = data_search("HighPress", date_during, "", "", ";", 0, 1)
    PowerLoadMax_real = data_search(predict_type, date_during, "", "", ";", 0, 1)


    pre_best_i = 0
    pre_best_j = 0

    for date_index in range(len(date_predict)):
        date_during = " where date < '" + date_predict[date_index] + "'"
        #season = " and date in (select date from date where season = (select season from date where date = '" + \
        #         date_predict[date_index] + "') and week = (select week from date where date = '" + \
        #         date_predict[date_index] + "'))"
        season = " and date in (select date from date where season = (select season from date where date = '" + \
                  date_predict[date_index] + "'))"
        holiday = " and date in (select date from date where holiday = (select holiday from date where date = '" + \
                  date_predict[date_index] + "') and week = (select week from date where date = '" + \
                  date_predict[date_index] + "'))"
        #holiday = " and date in (select date from date where holiday = (select holiday from date where date = '" + \
        #          date_predict[date_index] + "'))"
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
        PowerLoadMax = data_search(predict_type, date_during, season, holiday, finish_signal, 1, 1)

        #print(data_history)

        history_1 = pre_week(data_history, predict_type, 1)
        history_2 = pre_week(data_history, predict_type, 2)
        history_3 = pre_week(data_history, predict_type, 3)
        history_4 = pre_week(data_history, predict_type, 4)
        history_5 = pre_week(data_history, predict_type, 5)
        history_6 = pre_week(data_history, predict_type, 6)
        history_7 = pre_week(data_history, predict_type, 7)

        current_data = []
        current_data.append(AverTemper_predict[date_index])
        current_data.append(AverPress_predict[date_index])
        current_data.append(AverSPress_predict[date_index])
        current_data.append(LowTemper_predict[date_index])
        current_data.append(HighTemper_predict[date_index])
        current_data.append(LowPress_predict[date_index])
        current_data.append(HighPress_predict[date_index])
        current_data.append(history_1[len(history_1) - 1])
        current_data.append(history_2[len(history_2) - 1])
        current_data.append(history_3[len(history_3) - 1])
        current_data.append(history_4[len(history_4) - 1])
        current_data.append(history_5[len(history_5) - 1])
        current_data.append(history_6[len(history_6) - 1])
        current_data.append(history_7[len(history_7) - 1])
        #print(current_data)

        samplein = np.mat([AverTemper, AverPress, AverSPress, LowTemper, HighTemper, LowPress, HighPress, history_1, history_2, history_3, history_4, history_5, history_6, history_7])
        #print(samplein)
        sample_predict = np.mat([current_data, ] * len(data_history)).T
        sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0], samplein.max(axis=1).T.tolist()[0]]).transpose()
        sampleinnorm = ((np.array(samplein.T) - sampleinminmax.transpose()[0]) / (
            sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()
        sample_predictnorm = ((np.array(sample_predict.T) - sampleinminmax.transpose()[0]) / (
            sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()

        sample_temp = sampleinnorm - sample_predictnorm

        #得到当前日期最优解参数
        predict_finalresult = MaxValue
        current_best_i,current_best_j = 0,0
        for mu_index in range(len(muList)):
            for sigma_index in range(len(sigmaList)):
                SIMMartrix = np.zeros([sample_temp.shape[0], sample_temp.shape[1]])
                SIMCount = [0, ] * sample_temp.shape[1]

                for row in range(sample_temp.shape[0]):
                    for column in range(sample_temp.shape[1]):
                        if np.exp(-(sample_temp[row][column] ** 2) / (2 * sigmaList[sigma_index] * sigmaList[sigma_index])) >= muList[mu_index]:
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
                        SVM_X.append(
                            [AverTemper[i], AverPress[i], AverSPress[i], LowTemper[i], HighTemper[i], LowPress[i],
                             HighPress[i], history_1[i], history_2[i], history_3[i], history_4[i], history_5[i],
                             history_6[i], history_7[i]])
                        SVM_y.append(PowerLoadMax[i])

                predict_result = algorithm_SVM(SVM_X,SVM_y,current_data)
                if abs(predict_result - PowerLoadMax_real[date_index]) <= abs(predict_finalresult - PowerLoadMax_real[date_index]):
                    predict_finalresult = predict_result
                    current_best_i = mu_index
                    current_best_j = sigma_index
        #print(current_best_i,current_best_j)

        #通过上次的最优解参数得到当前日期的预测值
        SIMMartrix = np.zeros([sample_temp.shape[0], sample_temp.shape[1]])
        SIMCount = [0, ] * sample_temp.shape[1]

        for row in range(sample_temp.shape[0]):
            for column in range(sample_temp.shape[1]):
                if np.exp(-(sample_temp[row][column] ** 2) / (2 * sigmaList[pre_best_j] * sigmaList[pre_best_j])) >= muList[pre_best_i]:
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
                SVM_X.append(
                    [AverTemper[i], AverPress[i], AverSPress[i], LowTemper[i], HighTemper[i], LowPress[i],
                     HighPress[i], history_1[i], history_2[i], history_3[i], history_4[i], history_5[i],
                     history_6[i], history_7[i]])
                SVM_y.append(PowerLoadMax[i])

        current_predict_result = algorithm_SVM(SVM_X,SVM_y,current_data)

        SVM_result.append(current_predict_result)
        pre_best_i = current_best_i
        pre_best_j = current_best_j

    # 计算MAPE\MASE
    MAPE = CalMAPE(PowerLoadMax_real, SVM_result)
    MASE = CalMASE(PowerLoadMax_real, SVM_result)
    print("MAPE:" + str(round(MAPE * 100,2)) + "%")
    print("MASE:" + str(round(MASE * 100, 2)) + "%")
    return PredictList(date_predict, PowerLoadMax_real, SVM_result, MAPE)

def algorithm_SVM(X,y,test):
    clf = svm.SVR(gamma='auto', C=75, epsilon=50)
    clf.fit(X, y)
    result = round(float(clf.predict(test)), 2)
    return result

if __name__ == '__main__':
    start_date = ["2007-1-1","2007-2-1","2007-3-1","2007-4-1","2007-5-1","2007-6-1","2007-7-1","2007-8-1","2007-9-1","2007-10-1","2007-11-1","2007-12-1"]
    end_date = ["2007-1-31","2007-2-28","2007-3-31","2007-4-30","2007-5-31","2007-6-30","2007-7-31","2007-8-31","2007-9-30","2007-10-31","2007-11-30","2007-12-31"]
    for i in range(len(start_date)):
       print("start:" + start_date[i] + "---end:" + end_date[i])
       Result = Predict_Main(start_date[i], end_date[i])
    Result = Predict_Main()
    #print(Result.date)
    #print(Result.real)
    #print(Result.predict)
