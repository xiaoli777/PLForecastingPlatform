import pymysql

class DayData:
    def __init__(self,date = "",real = 0,predict = 0,offset = 0,MAPE = 0):
        self.date = date
        self.real = real
        self.predict = predict
        self.offset = offset
        self.MAPE = MAPE


def Access_Line(type,algorithm,date):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()

    DataList = []
    Data = []

    Count = cur.execute("select real_value from output where date = '" + date
                        + "' and Algorithm_Name = '" + algorithm + "' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList.append(('%s' % r))
    cur.scroll(0, mode='absolute')

    Count = cur.execute("select predict_value from output where date = '" + date
                        + "' and Algorithm_Name = '" + algorithm + "' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList.append(('%s' % r))
    cur.scroll(0, mode='absolute')

    for dl in DataList:
        dl = float(dl)
        Data.append(dl)
    #print(Data)

    MAPE = abs(Data[0] - Data[1]) / Data[0]

    cur.close()
    conn.close()

    return DayData(date,Data[0],Data[1],abs(Data[0] - Data[1]),MAPE)

if __name__ == '__main__':
    Preidct_Type = "Aver"
    Preidct_Algorithm = "AverValue"
    Selectedtime = "2005-1-1"
    result = Access_Line(Preidct_Type,Preidct_Algorithm,Selectedtime)
    print(result.date,result.real,result.predict,result.offset,result.MAPE)
