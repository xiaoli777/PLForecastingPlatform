import pymysql

class DataOutPutList:
    def __init__(self,AttributeList = [], DataList = []):
        self.AttributeList = AttributeList
        self.DataList = DataList

def DateTotalShow():
    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload')
    cur = conn.cursor()

    DateList_name = []
    TotalData = []

    Count = cur.execute('show columns from date;')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateList_name.append(('%s' % r[0]))
    #print(DateList_name)
    cur.scroll(0, mode='absolute')

    for dla in DateList_name:
        Count = cur.execute('select ' + dla + ' from date;')
        results = cur.fetchall()
        result = list(results)
        temp = []
        for r in result:
            temp.append(('%s' % r))
        #print(temp)
        TotalData.append(temp)
        cur.scroll(0, mode='absolute')
    #print(TotalData)
    cur.close()
    conn.close()
    #print(Count)
    return DataOutPutList(DateList_name,[[row[i] for row in TotalData] for i in range(len(TotalData[0]))])

def WeatherTotalShow():
    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload')
    cur = conn.cursor()

    DateList_name = []
    TotalData = []

    Count = cur.execute('show columns from data;')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateList_name.append(('%s' % r[0]))
    #print(DateList_name)
    cur.scroll(0, mode='absolute')

    for dla in DateList_name:
        Count = cur.execute('select ' + dla + ' from data;')
        results = cur.fetchall()
        result = list(results)
        temp = []
        for r in result:
            temp.append(('%s' % r))
        #print(temp)
        TotalData.append(temp)
        cur.scroll(0, mode='absolute')
    #print(TotalData)
    cur.close()
    conn.close()
    #print(Count)
    return DataOutPutList(DateList_name,[[row[i] for row in TotalData] for i in range(len(TotalData[0]))])

def TotalOutputShow():
    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload')
    cur = conn.cursor()

    DateList_name = []
    TotalData = []

    Count = cur.execute('show columns from output;')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateList_name.append(('%s' % r[0]))
    #print(DateList_name)
    cur.scroll(0, mode='absolute')

    for dla in DateList_name:
        Count = cur.execute('select ' + dla + ' from output;')
        results = cur.fetchall()
        result = list(results)
        temp = []
        for r in result:
            temp.append(('%s' % r))
        #print(temp)
        TotalData.append(temp)
        cur.scroll(0, mode='absolute')
    #print(TotalData)
    cur.close()
    conn.close()
    #print(Count)
    return DataOutPutList(DateList_name,[[row[i] for row in TotalData] for i in range(len(TotalData[0]))])

def OrderByHearder(tab,header,flag):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()

    DateList_name = []
    TotalData = []

    Count = cur.execute('show columns from ' + tab + ';')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateList_name.append(('%s' % r[0]))
    # print(DateList_name)
    cur.scroll(0, mode='absolute')

    for dla in DateList_name:
        if flag:
            Count = cur.execute('select ' + dla + ' from ' + tab + ' order by ' + header + ";")
        else:
            Count = cur.execute('select ' + dla + ' from ' + tab + ' order by ' + header + " desc;")
        results = cur.fetchall()
        result = list(results)
        temp = []
        for r in result:
            temp.append(('%s' % r))
        #print(temp)
        TotalData.append(temp)
        cur.scroll(0, mode='absolute')
        #print(TotalData)

    cur.close()
    conn.close()
    # print(Count)
    return DataOutPutList(DateList_name, [[row[i] for row in TotalData] for i in range(len(TotalData[0]))])
def DoubleClickedItem(DB_neme, Attribute_name, ClickedItem):
    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload')
    cur = conn.cursor()

    DateList_name = []
    TotalData = []

    Count = cur.execute('show columns from ' + DB_neme  +';')
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateList_name.append(('%s' % r[0]))
    cur.scroll(0, mode='absolute')


    for dla in DateList_name:
        Count = cur.execute('select ' + dla + ' from ' + DB_neme  +' where ' + Attribute_name + ' >= ' + ClickedItem
                            + ' and ' + Attribute_name + ' <= ' + ClickedItem + ';')
        results = cur.fetchall()
        result = list(results)
        temp = []
        for r in result:
            temp.append(('%s' % r))
        TotalData.append(temp)
        cur.scroll(0, mode='absolute')
    cur.close()
    conn.close()
    return DataOutPutList(DateList_name,[[row[i] for row in TotalData] for i in range(len(TotalData[0]))])


if __name__ == '__main__':
   result = DoubleClickedItem("data", 'Date', '2007-01-04')
   print(result.AttributeList)
   print(result.DataList)