import pymysql

#name = "测试算法"

class PredictList:
    def __init__(self,date = [], real = [], predict =[], MAPE = 0):
        self.date = date
        self.real = real
        self.predict = predict
        self.MAPE = MAPE

def Predict_Main(date_start = "2007-1-1",date_end = "2007-1-31",paramter = 7,predicttype = "Max"):
    date_predict = []
    real_resultList = []
    real_result = []
    predict_result = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    Count = cur.execute('select date from data where date >= "'
                        + date_start + '" and date <= "' + date_end + '";')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        date_predict.append(('%s' % r))
    cur.scroll(0, mode='absolute')

    Count = cur.execute('select PowerLoadMax from data where date >= "'
                        + date_start + '" and date <= "' + date_end + '";')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        real_resultList.append(("%s" % r))

    for pl in real_resultList:
        pl = float(pl)
        real_result.append(pl)
        predict_result.append(round(pl * 2 - 5000,2))
    cur.scroll(0, mode='absolute')

    cur.close()
    conn.close()
    print("This app is running!")
    return PredictList(date_predict,real_result,predict_result)

if __name__ == '__main__':
    Result = Predict_Main()
    print(Result.date)
    print(Result.real)
    print(Result.predict)