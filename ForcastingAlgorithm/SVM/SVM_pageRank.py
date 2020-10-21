"""
第四代：仅对未来进行预测，使用未来数据，不使用预测数据,对一些异常点单独测试，模块化，SVM预测模型
"""
import pymysql
import numpy as np
import math
from sklearn import svm
import warnings

name = "SVM回归分析"
Threshold = 365
sigma = 0.5 #math.sqrt(0.5)
mu = 0.9

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

def pre_week(date_list, predict_type, index):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()
    current_data_list = []

    for date in date_list:
        current_data = []
        Count = cur.execute('select ' + predict_type + ' from data '
                                                       'where date = DATE_SUB("' + date + '",'
                                                                                          'INTERVAL ' + str(
            index) + ' DAY);')
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

def train_date(date, para = 1):
    date_during = " where date < '" + date + "'"
    season = " and date in (select date from date where season = (select season from date where date = '" + \
             date + "'))"
    holiday = " and date in (select date from date where holiday = (select holiday from date where date = '" + \
              date + "') and week = (select week from date where date = '" + \
              date + "'))"
    finish_signal = ";"

    if para == 1:
        season = ""
        holiday = ""
    elif para == 3:
        holiday = ""
    elif para == 5:
        season = ""
    else:
        pass

    data_history = data_search("date", date_during, season, holiday, finish_signal, 1, 0) + [date, ]

    return data_history

def train_feature(date_list, name):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()
    datalist = []

    for date in date_list:
        current_data = []
        Count = cur.execute('select ' + name + ' from data '
                                               'where date = "' + date + '";')

        results = cur.fetchall()
        result = list(results)
        for r in result:
            current_data.append(('%s' % r))
        for num in current_data:
            num = float(num)
            datalist.append(num)

    cur.close()
    conn.close()
    return datalist

def train_select(date, predict_type, paramter=1):
    data_history = train_date(date, paramter)
    AverTemper = train_feature(data_history, 'AverTemper')
    AverPress = train_feature(data_history, 'AverPress')
    AverSPress = train_feature(data_history, 'AverSPress')
    LowTemper = train_feature(data_history, 'LowTemper')
    HighTemper = train_feature(data_history, 'HighTemper')
    LowPress = train_feature(data_history, 'LowPress')
    HighPress = train_feature(data_history, 'HighPress')

    history_1 = pre_week(data_history, predict_type, 1)
    history_2 = pre_week(data_history, predict_type, 2)
    history_3 = pre_week(data_history, predict_type, 3)
    history_4 = pre_week(data_history, predict_type, 4)
    history_5 = pre_week(data_history, predict_type, 5)
    history_6 = pre_week(data_history, predict_type, 6)
    history_7 = pre_week(data_history, predict_type, 7)

    samplein = np.mat([AverTemper, AverPress, AverSPress, LowTemper, HighTemper, LowPress, HighPress, history_1, history_2, history_3,history_4, history_5, history_6, history_7])
    sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0], samplein.max(axis=1).T.tolist()[0]]).transpose()
    sampleinnorm = ((np.array(samplein.T) - sampleinminmax.transpose()[0]) / (sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0]))

    SIMMartrix = np.zeros([sampleinnorm.shape[0], sampleinnorm.shape[0]])

    for i in range(len(sampleinnorm)):
        for j in range(len(sampleinnorm)):
            Count = 0
            for k in range(len(sampleinnorm[0])):
                #if np.exp(- (abs(sampleinnorm[j][k] - sampleinnorm[i][k]) ** 2) / (2 * sigma * sigma)) >= mu:
                if np.exp(- (abs(sampleinnorm[j][k] - sampleinnorm[i][k]) ) / (2 * sigma * sigma)) >= mu:
                    Count = Count + 1
            if i == j:
                SIMMartrix[i][j] = 0
            else:
                SIMMartrix[i][j] = Count

    # for i in range(len(SIMMartrix)):
    #     Count = 0
    #     for j in range(len(SIMMartrix[i])):
    #         Count = Count + SIMMartrix[i][j]
    #     SIMMartrix[i] = (SIMMartrix[i] / Count)

    for i in range(len(SIMMartrix)):
        SIMMartrix[i] = SIMMartrix[i] / SIMMartrix[i].sum()

    SIMMartrix_transpose = SIMMartrix.transpose()

    SIMMartrix_transpose = np.mat(SIMMartrix_transpose)
    p0 = np.zeros([sampleinnorm.shape[0], 1])
    p0[-1] = 1
    p0 = np.mat(p0)
    pt = p0
    gamma = 0.7

    # temp1 = SIMMartrix_transpose * p0
    # temp2 = SIMMartrix_transpose * temp1
    # print((abs(temp1 - temp2)).sum())

    Count = 0
    while(1):
        ptemp = (1 - gamma) * SIMMartrix_transpose * pt + gamma * p0
        diff = (abs(ptemp - pt)).sum()
        pt = ptemp
        if diff <= (10 ** (-6)):
            break
        Count = Count + 1

        #print(str(Count) + ":" + str(diff))

    date_list = []
    date_Count = 30
    for i in range(date_Count):
        value_max = 0
        value_max_index = 0
        for j in range(len(pt) - 1):
            if pt[j] > value_max:
                value_max = pt[j]
                value_max_index = j
        pt[value_max_index] = 0
        date_list.append(data_history[value_max_index])

    date_list = list(set(date_list))
    print(date_list)

    return date_list

def algorithm_SVM(X, y):
    clf = svm.SVR(gamma='auto', C=75, epsilon=50)
    clf.fit(X[:-1], y[:-1])
    result = round(float(clf.predict(X[-1])), 2)
    return result

def Predict_Main(date_start="2007-1-1", date_end="2007-12-31", paramter = 1, predicttype="Max"):
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
    results = cur.fetchall()
    result = list(results)
    for r in result:
        date_predict.append(('%s' % r))
    date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"

    cur.scroll(0, mode='absolute')
    cur.close()
    conn.close()

    PowerLoadMax_real = data_search(predict_type, date_during, "", "", ";", 0, 1)

    for date_index in range(len(date_predict)):
        date_List = train_select(date_predict[date_index], predict_type, paramter) + [date_predict[date_index],]
        #print(date_List)

        AverTemper = train_feature(date_List, 'AverTemper')
        AverPress = train_feature(date_List, 'AverPress')
        AverSPress = train_feature(date_List, 'AverSPress')
        LowTemper = train_feature(date_List, 'LowTemper')
        HighTemper = train_feature(date_List, 'HighTemper')
        LowPress = train_feature(date_List, 'LowPress')
        HighPress = train_feature(date_List, 'HighPress')
        PowerLoadMax = train_feature(date_List, predict_type)

        history_1 = pre_week(date_List, predict_type, 1)
        history_2 = pre_week(date_List, predict_type, 2)
        history_3 = pre_week(date_List, predict_type, 3)
        history_4 = pre_week(date_List, predict_type, 4)
        history_5 = pre_week(date_List, predict_type, 5)
        history_6 = pre_week(date_List, predict_type, 6)
        history_7 = pre_week(date_List, predict_type, 7)

        SVM_X = []
        SVM_y = []
        for i in range(len(date_List)):
            SVM_X.append(
                [AverTemper[i], AverPress[i], AverSPress[i], LowTemper[i], HighTemper[i], LowPress[i],
                 HighPress[i], history_1[i], history_2[i], history_3[i], history_4[i], history_5[i],
                 history_6[i], history_7[i]])
            SVM_y.append(PowerLoadMax[i])

        current_predict_result = algorithm_SVM(SVM_X, SVM_y)
        SVM_result.append(current_predict_result)

    # 计算MAPE\MASE
    MAPE = CalMAPE(PowerLoadMax_real, SVM_result)
    MASE = CalMASE(PowerLoadMax_real, SVM_result)
    print("MAPE:" + str(round(MAPE * 100, 2)) + "%")
    print("MASE:" + str(round(MASE * 100, 2)) + "%")
    return PredictList(date_predict, PowerLoadMax_real, SVM_result, MAPE)

if __name__ == '__main__':
    # start_date = ["2007-1-1", "2007-2-1", "2007-3-1", "2007-4-1", "2007-5-1", "2007-6-1", "2007-7-1", "2007-8-1",
    #               "2007-9-1", "2007-10-1", "2007-11-1", "2007-12-1"]
    # end_date = ["2007-1-31", "2007-2-28", "2007-3-31", "2007-4-30", "2007-5-31", "2007-6-30", "2007-7-31", "2007-8-31",
    #             "2007-9-30", "2007-10-31", "2007-11-30", "2007-12-31"]
    # for i in range(len(start_date)):
    #     print("start:" + start_date[i] + "---end:" + end_date[i])
    #     Result = Predict_Main(start_date[i], end_date[i])
    Result = Predict_Main("2007-1-1","2007-1-31")