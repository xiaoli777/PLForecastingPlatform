import pymysql

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
        if Count > 30:
            Temp = TempList[Count-30:]
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

date_start = "2005-5-1"
date_end = "2005-5-28"
predict_type = 1
paramter = 7

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

# print(date_predict)
# print(AverTemper_predict)
# print(AverPress_predict)
# print(AverSPress_predict)
# print(LowTemper_predict)
# print(HighTemper_predict)
# print(LowPress_predict)
# print(HighPress_predict)

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

    date_history = data_search("date",date_during,season,holiday,finish_signal,1,0)
    AverTemper = data_search("AverTemper",date_during,season,holiday,finish_signal,1,1)
    AverPress = data_search("AverPress",date_during,season,holiday,finish_signal,1,1)
    AverSPress = data_search("AverSPress",date_during,season,holiday,finish_signal,1,1)
    LowTemper = data_search("LowTemper",date_during,season,holiday,finish_signal,1,1)
    HighTemper = data_search("HighTemper",date_during,season,holiday,finish_signal,1,1)
    LowPress = data_search("LowPress",date_during,season,holiday,finish_signal,1,1)
    HighPress = data_search("HighPress",date_during,season,holiday,finish_signal,1,1)
    PowerLoadMax = data_search("PowerLoadMax",date_during,season,holiday,finish_signal,1,1)

    # print(date_history)
    # print(AverTemper)
    # print(AverPress)
    # print(AverSPress)
    # print(LowTemper)
    # print(HighTemper)
    # print(LowPress)
    # print(HighPress)
    # print(PowerLoadMax)

    date_history = []
    AverTemper = []
    AverPress = []
    AverSPress = []
    LowTemper = []
    HighTemper = []
    LowPress = []
    HighPress = []
    PowerLoadMax = []

print(date_predict)

#conn.commit()
cur.close()
conn.close()