import pymysql

class ScatterPoint:
    def __init__(self,tab_1 = [],tab_2 = []):
        self.tab_1 = tab_1
        self.tab_2 = tab_2


def Access_Point(Table_name_1,Table_name_2,start,end):
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')
    cur = conn.cursor()

    DataList1 = []
    Data1 = []
    DataList2 = []
    Data2 = []

    Count = cur.execute("select " + Table_name_1 + " from data where date between '" + start + "' and '"+ end + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList1.append(('%s' % r))
    cur.scroll(0, mode='absolute')

    for dl in DataList1:
        dl = float(dl)
        Data1.append(dl)
    #print(Data1)

    Count = cur.execute("select " + Table_name_2 + " from data where date between '" + start + "' and '" + end + "';")
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DataList2.append(('%s' % r))
    cur.scroll(0, mode='absolute')

    for dl in DataList2:
        dl = float(dl)
        Data2.append(dl)
    #print(Data2)

    cur.close()
    conn.close()

    return ScatterPoint(Data1,Data2)

if __name__ == '__main__':
    Table_name_11 = "PowerLoadMin"
    Table_name_22 = "AverTemper"
    start_time = "2005-1-1"
    end_time = "2005-2-1"
    result = Access_Point(Table_name_11,Table_name_22,start_time,end_time)
