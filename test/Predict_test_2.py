"""
第一代：仅对未来进行预测，未来数据、预测数据均不使用
"""

import pymysql
import numpy as np
import datetime
import math
import matplotlib.pyplot as plt

date_start = "2007-1-1"
date_end = "2007-12-31"
predict_type = 1
paramter = 7
Threshold = 150
sigma = math.sqrt(0.5)
mu = 0.95   #0.95
gamma = 0.126

def data_search(searchtype,dd,ss,hld,fs,type = 1,datatype = 1):
    TempList = []
    Temp = []
    Count = cur.execute('select ' + searchtype + ' from datasetH' + dd + ss + hld + fs)
    #print(Count)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        TempList.append(('%s' % r))
    #print(TempList)
    if type == 1:
        if Count > Threshold:
            Temp = TempList[Count-Threshold:]
        else:
            Temp = TempList
    else:
        Temp = TempList
    cur.scroll(0, mode='absolute')
    # print(Temp)
    if datatype == 1:
        TempList = []
        for num in Temp:
            num = float(num)
            TempList.append(num)
        return TempList
    else:
        cur.scroll(0,mode='absolute')
        return Temp

def CalDays(date_1,date_2):
    time_1 = datetime.datetime.strptime(date_1,'%Y-%m-%d')
    time_2 = datetime.datetime.strptime(date_2,'%Y-%m-%d')
    # print(time_1,time_2)
    result = (time_2 - time_1).days
    # print(result)
    return result

date_predict = []
AverTemper_predict = []
AverPress_predict = []
AverSPress_predict = []
LowTemper_predict = []
HighTemper_predict = []
LowPress_predict = []
HighPress_predict = []
PowerLoadMax_predict = []

date_history = []
AverTemper = []
AverPress = []
AverSPress = []
LowTemper = []
HighTemper = []
LowPress = []
HighPress = []
PowerLoadMax_real = []
PowerLoadMax = []

conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='pl') #db：库名
cur = conn.cursor()

date_during = ""
if predict_type:
    Count = cur.execute('select date from datasetH where date >= "'
                        + date_start + '" and date <= "' + date_end + '";')
    if Count == 0:
        print("数据库中无数据！")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        date_predict.append(('%s' % r))
    date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"
else:
    Count = cur.execute('select date from datasetH where date = "' + date_start + '";')
    if Count == 0:
        print("数据库中无此数据！")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        date_predict.append(('%s' % r))
    date_during = " where date = '" + date_start + "'"
cur.scroll(0,mode='absolute')

AverTemper_predict = data_search("AverTemper",date_during,"","",";",0,1)
AverPress_predict = data_search("AverPress",date_during,"","",";",0,1)
AverSPress_predict = data_search("AverSPress",date_during,"","",";",0,1)
LowTemper_predict = data_search("LowTemper",date_during,"","",";",0,1)
HighTemper_predict = data_search("HighTemper",date_during,"","",";",0,1)
LowPress_predict = data_search("LowPress",date_during,"","",";",0,1)
HighPress_predict = data_search("HighPress",date_during,"","",";",0,1)
PowerLoadMax_real = data_search("PowerLoadMax",date_during,"","",";",0,1)
PowerLoadMax = data_search("PowerLoadMax",date_during,"","",";",0,1)

# print(date_predict)
# print(AverTemper_predict)
# print(AverPress_predict)
# print(AverSPress_predict)
# print(LowTemper_predict)
# print(HighTemper_predict)
# print(LowPress_predict)
# print(HighPress_predict)
# print(PowerLoadMax_real)

for date_index in range(len(date_predict)):
    date_during = " where date < '" + date_start + "'"
    season = " and season = (select season from datasetH where date = '" + date_predict[date_index] + "')"
    holiday = " and holiday = (select holiday from datasetH where date = '" + date_predict[date_index] + "')"
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

    #print(holiday)
    #print(season)

    data_history = data_search("date",date_during,season,holiday,finish_signal,1,0)\
                   + [date_predict[date_index],]
    AverTemper = data_search("AverTemper",date_during,season,holiday,finish_signal,1,1)\
                 + [AverTemper_predict[date_index],]
    AverPress = data_search("AverPress",date_during,season,holiday,finish_signal,1,1)\
                + [AverPress_predict[date_index],]
    AverSPress = data_search("AverSPress",date_during,season,holiday,finish_signal,1,1)\
                 + [AverSPress_predict[date_index],]
    LowTemper = data_search("LowTemper",date_during,season,holiday,finish_signal,1,1)\
                + [LowTemper_predict[date_index],]
    HighTemper = data_search("HighTemper",date_during,season,holiday,finish_signal,1,1)\
                 + [HighTemper_predict[date_index],]
    LowPress = data_search("LowPress",date_during,season,holiday,finish_signal,1,1)\
               + [LowPress_predict[date_index],]
    HighPress = data_search("HighPress",date_during,season,holiday,finish_signal,1,1)\
                + [HighPress_predict[date_index],]
    PowerLoadMax = data_search("PowerLoadMax",date_during,season,holiday,finish_signal,1,1)

    current_data = []
    current_data.append(AverTemper_predict[date_index])
    current_data.append(AverPress_predict[date_index])
    current_data.append(AverSPress_predict[date_index])
    current_data.append(LowTemper_predict[date_index])
    current_data.append(HighTemper_predict[date_index])
    current_data.append(LowPress_predict[date_index])
    current_data.append(HighPress_predict[date_index])
    #print(current_data)

    # date_history = data_search("date", date_during, season, holiday, finish_signal, 1, 0)
    # AverTemper = data_search("AverTemper", date_during, season, holiday, finish_signal, 1, 1)
    # AverPress = data_search("AverPress", date_during, season, holiday, finish_signal, 1, 1)
    # AverSPress = data_search("AverSPress", date_during, season, holiday, finish_signal, 1, 1)
    # LowTemper = data_search("LowTemper", date_during, season, holiday, finish_signal, 1, 1)
    # HighTemper = data_search("HighTemper", date_during, season, holiday, finish_signal, 1, 1)
    # LowPress = data_search("LowPress", date_during, season, holiday, finish_signal, 1, 1)
    # HighPress = data_search("HighPress", date_during, season, holiday, finish_signal, 1, 1)
    # PowerLoadMax = data_search("PowerLoadMax", date_during, season, holiday, finish_signal, 1, 1)

    samplein = np.mat([AverTemper, AverPress, AverSPress, LowTemper, HighTemper, LowPress, HighPress])
    sample_predict = np.mat([current_data,] * len(data_history)).T
    sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0], samplein.max(axis=1).T.tolist()[0]]).transpose()
    sampleinnorm = ((np.array(samplein.T) - sampleinminmax.transpose()[0]) / (sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()
    sample_predictnorm = ((np.array(sample_predict.T) - sampleinminmax.transpose()[0]) / (sampleinminmax.transpose()[1] - sampleinminmax.transpose()[0])).transpose()

    sample_temp = sampleinnorm - sample_predictnorm
    SIMMartrix = np.zeros([sample_temp.shape[0],sample_temp.shape[1]])
    SIMCount = [0,] * sample_temp.shape[1]

    #print(sample_predictnorm.shape[0],sample_predictnorm.shape[1],sample_predictnorm.shape)

    for row in range(sample_temp.shape[0]):
        for column in range(sample_temp.shape[1]):
            if np.exp(-(sample_temp[row][column] ** 2)/(2 * sigma * sigma)) >= mu:
                SIMMartrix[row][column] = 1
                SIMCount[column] += 1
            else:
                SIMMartrix[row][column] = 0

    # print(SIMMartrix)
    #print(SIMCount)

    SIMCount.pop()
    #print(max(SIMCount))
    #print(SIMCount)
    # print(PowerLoadMax)
    SumPowerLoadMax_pridict = 0
    MaxIndexCount = 0
    for i in range(len(SIMCount)):
        if SIMCount[i] == max(SIMCount):
            MaxIndexCount += 1
            IntervelDays = CalDays(data_history[i],date_predict[date_index])
            #print(data_history[i], PowerLoadMax[i])
            #print(IntervelDays)
            #print(PowerLoadMax[i] * (1 + gamma * (IntervelDays / 365)))
            SumPowerLoadMax_pridict += (PowerLoadMax[i] * (1 + gamma * (IntervelDays / 365)))
            #print(SumPowerLoadMax_pridict)

    PowerLoadMax_predict.append(round((SumPowerLoadMax_pridict / MaxIndexCount),2))

    # print(sample_predict)
    # print(date_history)
    # print(AverTemper)
    # print(AverPress)
    # print(AverSPress)
    # print(LowTemper)
    # print(HighTemper)
    # print(LowPress)
    # print(HighPress)
    # print(PowerLoadMax)
    # print(samplein)
    # print(sampleinminmax)
    # print(sampleinnorm)
    # print(sample_predictnorm)
    #print(sampleinnorm - sample_predictnorm)

    date_history = []
    AverTemper = []
    AverPress = []
    AverSPress = []
    LowTemper = []
    HighTemper = []
    LowPress = []
    HighPress = []
    PowerLoadMax = []

print(PowerLoadMax_real)
# print(date_predict)
print(PowerLoadMax_predict)

DateAmend = []
index = 0
for da in date_predict:
    if len(date_predict) >= 10:
        if index % 3 == 0:
            da = da[5:]
        else:
            da = ""
        index = index + 1
    else:
        da = da[5:]
    DateAmend.append(da)
# print(DateAmend)

#conn.commit()
cur.close()
conn.close()

# 预测输出和实际输出对比图
plt.figure('电力负荷实际 & 预测')
ax=plt.gca()
line1, = ax.plot(PowerLoadMax_real,'k',marker = u'$\circ$')
line2, = ax.plot(PowerLoadMax_predict,'r',markeredgecolor='b',marker = u'$\star$',markersize=9)

ax.legend((line1,line2),('real output','predict output'),loc = 'upper left')

yticks = range(4000,6500,500)
ytickslabel = range(4000,6500,500)
ax.set_yticks(yticks)
ax.set_yticklabels(ytickslabel)
ax.set_ylabel(u'Power Load')

xticks = range(0,len(DateAmend),1)
xtickslabel = DateAmend
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabel)
ax.set_xlabel(u'Date')
ax.set_title('Power Load Real & Predict')

# plt.show()
plt.close()

# 计算MAPE
SumMAPE = 0
for pl in range(len(PowerLoadMax_real)):
    SumMAPE += abs(PowerLoadMax_predict[pl] - PowerLoadMax_real[pl]) / PowerLoadMax_real[pl]
MAPE = SumMAPE / len(PowerLoadMax_real)
print("MAPE : " + str(round(MAPE,4)*100) + "%")