import pymysql


class SquareList:
    def __init__(self, SList=[], TList=[], DList=[]):
        self.SList = SList
        self.TList = TList
        self.DList = DList


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def CalMAPE(Algorithm, year, start, end,type = "Max"):
    DataList_predict = []
    Data_predict = []
    DataList_real = []
    Data_real = []
    MAPEList = []
    TimeList = []
    Detail = []
    DetailList = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()
    if year:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select predict_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_predict.append(('%s' % r))

            # print(DataList_predict)
            for dp in DataList_predict:
                dp = float(dp)
                Data_predict.append(dp)
            # print(Data_predict)
            cur.scroll(0, mode='absolute')

            Count = cur.execute("select real_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            SumMAPE = 0
            # print(len(Data_predict))
            for pl in range(len(Data_predict)):
                Detail.append(round((abs(Data_predict[pl] - Data_real[pl]) / Data_real[pl]) * 100, 2))
                SumMAPE += abs(Data_predict[pl] - Data_real[pl]) / Data_real[pl]
            MAPEList.append(round(SumMAPE / len(Data_real) * 100, 2))
            TimeList.append(i)
            DetailList.append(Detail)

            DataList_predict = []
            Data_predict = []
            DataList_real = []
            Data_real = []
            Detail = []
            # print(Count)
    else:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select predict_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_predict.append(('%s' % r))

            # print(DataList_predict)
            for dp in DataList_predict:
                dp = float(dp)
                Data_predict.append(dp)
            # print(Data_predict)
            cur.scroll(0, mode='absolute')

            Count = cur.execute("select real_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            SumMAPE = 0
            for pl in range(len(Data_predict)):
                SumMAPE += abs(Data_predict[pl] - Data_real[pl]) / Data_real[pl]
            MAPEList.append(round(SumMAPE / len(Data_real) * 100, 2))
            TimeList.append(i)
            tempValue = CalMAPE(Algorithm, i, 1, 12,type)
            #print(tempValue.SList)
            DetailList.append(tempValue.SList)

            DataList_predict = []
            Data_predict = []
            DataList_real = []
            Data_real = []

            # print(Count)
    # print(MAPEList,TimeList, DetailList)
    #print(DetailList)
    cur.close()
    conn.close()
    return SquareList(MAPEList, TimeList, DetailList)


def CalErrorMax(Algorithm, year, start, end, type = "Max"):
    DataList_predict = []
    Data_predict = []
    DataList_real = []
    Data_real = []
    MAPEList = []
    TimeList = []
    DetailList = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()
    if year:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select predict_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_predict.append(('%s' % r))

            # print(DataList_predict)
            for dp in DataList_predict:
                dp = float(dp)
                Data_predict.append(dp)
            # print(Data_predict)
            cur.scroll(0, mode='absolute')

            Count = cur.execute("select real_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            TempList = []
            for pl in range(len(Data_predict)):
                TempList.append(round((abs(Data_predict[pl] - Data_real[pl]) / Data_real[pl]) * 100, 2))
            MAPEList.append(max(TempList))
            TimeList.append(i)
            DetailList.append(TempList)

            DataList_predict = []
            Data_predict = []
            DataList_real = []
            Data_real = []
            # print(Count)
    else:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select predict_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_predict.append(('%s' % r))

            # print(DataList_predict)
            for dp in DataList_predict:
                dp = float(dp)
                Data_predict.append(dp)
            # print(Data_predict)
            cur.scroll(0, mode='absolute')

            Count = cur.execute("select real_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            TempList = []
            for pl in range(len(Data_predict)):
                TempList.append(round(((Data_predict[pl] - Data_real[pl]) / Data_real[pl]) * 100, 2))
            MAPEList.append(max(TempList) * 100)
            TimeList.append(i)
            tempValue = CalErrorMax(Algorithm, i, 1, 12, type)
            # print(tempValue.SList)
            DetailList.append(tempValue.SList)

            DataList_predict = []
            Data_predict = []
            DataList_real = []
            Data_real = []

            # print(Count)
    # print(MAPEList, TimeList)
    cur.close()
    conn.close()
    return SquareList(MAPEList, TimeList, DetailList)


def CalSum(Algorithm, year, start, end, type = "Max"):
    DataList_real = []
    Data_real = []
    MAPEList = []
    TimeList = []
    Detail = []
    DetailList = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()
    if year:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select real_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            SumValue = 0
            for pl in range(len(Data_real)):
                SumValue = SumValue + Data_real[pl]
                Detail.append(Data_real[pl])
            MAPEList.append(int(SumValue))
            TimeList.append(i)
            DetailList.append(Detail)

            DataList_real = []
            Data_real = []
            Detail = []
    else:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select real_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            SumValue = 0
            for pl in range(len(Data_real)):
                SumValue = SumValue + Data_real[pl]
            MAPEList.append(int(SumValue))
            TimeList.append(i)
            tempValue = CalSum(Algorithm, i, 1, 12, type)
            # print(tempValue.SList)
            DetailList.append(tempValue.SList)

            DataList_real = []
            Data_real = []
    # print(MAPEList, TimeList)
    cur.close()
    conn.close()
    return SquareList(MAPEList, TimeList, DetailList)


def CalMax(Algorithm, year, start, end, type = "Max"):
    DataList_real = []
    Data_real = []
    MAPEList = []
    TimeList = []
    DetailList = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()
    if year:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select real_value from output where date between '" +
                                str(year) + "-" + str(i) + "-" + str(1) + "' and '" +
                                str(year) + "-" + str(i) + "-" + str(days[i]) + "' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            MaxValue = []
            for pl in range(len(Data_real)):
                MaxValue.append(Data_real[pl])

            MAPEList.append(int(max(MaxValue)))
            TimeList.append(i)
            DetailList.append(MaxValue)

            DataList_real = []
            Data_real = []
    else:
        for i in range(start, end + 1, 1):
            Count = cur.execute("select real_value from output where date between '" +
                                str(i) + "-1-1' and '" + str(i) + "-12-31' and Algorithm_Name = '"
                                + Algorithm + "' and Predict_Type = '" + type + "';")
            results = cur.fetchall()
            result = list(results)
            for r in result:
                DataList_real.append(('%s' % r))
            # print(DataList_real)

            for dp in DataList_real:
                dp = float(dp)
                Data_real.append(dp)
            # print(Data_real)
            cur.scroll(0, mode='absolute')

            MaxValue = []
            for pl in range(len(Data_real)):
                MaxValue.append(Data_real[pl])
            MAPEList.append(int(max(MaxValue)))
            TimeList.append(i)
            tempValue = CalMax(Algorithm, i, 1, 12, type)
            # print(tempValue.SList)
            DetailList.append(tempValue.SList)

            DataList_real = []
            Data_real = []
    # print(MAPEList, TimeList)
    cur.close()
    conn.close()
    return SquareList(MAPEList, TimeList, DetailList)

def Algorithm_name_list():
    algorithm_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()

    Count = cur.execute("select distinct Algorithm_name from output;")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        algorithm_list.append(('%s' % r))
    print(algorithm_list)

    cur.close()
    conn.close()
    return algorithm_list

if __name__ == '__main__':
    Algorithm = "SVM"
    year = 0
    start = 2005
    end = 2007
    result = CalMAPE(Algorithm, year, start, end)
    print(result.SList, result.TList, result.DList)
    result = CalErrorMax(Algorithm, year, start, end)
    print(result.SList, result.TList, result.DList)
    result = CalSum(Algorithm, year, start, end)
    print(result.SList, result.TList, result.DList)
    result = CalMax(Algorithm, year, start, end)
    print(result.SList, result.TList, result.DList)
    Algorithm_name = Algorithm_name_list()
