import pymysql
import numpy as np
import math

class SimilarDays:
    def __init__(self, date = [], sign =[]):
        self.date = date
        self.sign = sign

def weather_search(item,date):
    TempList = []
    Temp = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    Count = cur.execute('select ' + item + ' from data where date <= "'
                        + date + '";')

    results = cur.fetchall()
    result = list(results)

    for r in result:
        TempList.append(('%s' % r))

    for t in TempList:
        t = float(t)
        Temp.append(t)
    cur.scroll(0, mode='absolute')

    cur.close()
    conn.close()

    return Temp[len(Temp) - 366:]

def Similar_Search(date = '2007-12-1',mu_temp = 0.95,sigma_temp = 0.5):
    mu = mu_temp
    sigma = math.sqrt(sigma_temp)
    DateList = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    Count = cur.execute('select date from data where date <= "'
                        + date + '";')

    results = cur.fetchall()
    result = list(results)

    for r in result:
        DateList.append(('%s' % r))

    cur.close()
    conn.close()

    DateList = DateList[len(DateList) - 366:]
    AverSPress = weather_search('AverSPress', date)
    LowTemper = weather_search('LowTemper', date)
    HighTemper = weather_search('HighTemper', date)
    AverTemper = weather_search('AverTemper', date)
    LowPress = weather_search('LowPress', date)
    HighPress = weather_search('HighPress', date)
    AverPress = weather_search('AverPress', date)

    current_data = []
    current_data.append(AverSPress[-1])
    current_data.append(LowTemper[-1])
    current_data.append(HighTemper[-1])
    current_data.append(AverTemper[-1])
    current_data.append(LowPress[-1])
    current_data.append(HighPress[-1])
    current_data.append(AverPress[-1])

    samplein = np.mat([AverSPress, LowTemper, HighTemper, AverTemper, LowPress, HighPress, AverPress])
    sample_predict = np.mat([current_data, ] * len(DateList)).T
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
    DateList.pop()
    return SimilarDays(DateList,SIMCount)


if __name__ == '__main__':
    Result = Similar_Search()
    print(Result.date)
    print(Result.sign)
