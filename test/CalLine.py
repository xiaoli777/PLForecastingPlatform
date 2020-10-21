import pymysql

class LineList:
    def __init__(self,TList = [],RList = [],SList = [],LList = [],AList = []):
        self.TList = TList
        self.RList = RList
        self.SList = SList
        self.LList = LList
        self.AList = AList

def Access_Line(type,start,end):
    DataList_predict_SVM = []
    Data_predict_SVM = []
    DataList_predict_linear = []
    Data_predict_linear = []
    DataList_predict_aver = []
    Data_predict_aver = []
    DataList_real = []
    Data_real = []
    DataList = []
    TimeList = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload', charset='utf8')
    cur = conn.cursor()

    Count = cur.execute("select date from date where date between '" +
                        start + "' and '" + end + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList.append(('%s' % r))
    cur.scroll(0, mode='absolute')
    print(DataList)

    Count = cur.execute("select real_value from output where date between '" +
                        start + "' and '" + end + "' and Algorithm_Name = 'SVM' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList_real.append(('%s' % r))

    for dp in DataList_real:
        dp = float(dp)
        Data_real.append(dp)
    cur.scroll(0, mode='absolute')
    print(Data_real)

    Count = cur.execute("select predict_value from output where date between '" +
                        start + "' and '" + end + "' and Algorithm_Name = 'SVM' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList_predict_SVM.append(('%s' % r))

    for dp in DataList_predict_SVM:
        dp = float(dp)
        Data_predict_SVM.append(dp)
    cur.scroll(0, mode='absolute')
    print(Data_predict_SVM)

    Count = cur.execute("select predict_value from output where date between '" +
                        start + "' and '" + end + "' and Algorithm_Name = 'MultiLinear' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList_predict_linear.append(('%s' % r))

    for dp in DataList_predict_linear:
        dp = float(dp)
        Data_predict_linear.append(dp)
    cur.scroll(0, mode='absolute')
    print(Data_predict_linear)

    Count = cur.execute("select predict_value from output where date between '" +
                        start + "' and '" + end + "' and Algorithm_Name = 'AverValue' and Predict_Type = '" + type + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList_predict_aver.append(('%s' % r))

    for dp in DataList_predict_aver:
        dp = float(dp)
        Data_predict_aver.append(dp)
    cur.scroll(0, mode='absolute')
    print(Data_predict_aver)

    cur.close()
    conn.close()
    return LineList(TimeList,Data_real,Data_predict_SVM,Data_predict_linear,Data_predict_aver)

if __name__ == '__main__':
    Preidct_Type = "Max"
    start = "2005-1-1"
    end = "2005-1-3"
    result = Access_Line(Preidct_Type,start,end)
