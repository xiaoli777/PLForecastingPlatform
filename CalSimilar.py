import pymysql

def Weather_Similar(date = '2005-1-1' , type = ""):
    result_list = []
    result = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload', charset='utf8')
    cur = conn.cursor()

    if type == "":
        Count = cur.execute("select * from data where date = '" + date + "';")
        results = list(cur.fetchall())

        for r in results[0][1:8]:
            result_list.append(('%s' % r))

        for r in result_list:
            re = int(r)
            result.append(re)
    elif type == "max":
        Count = cur.execute("select max(AverPress),max(HighPress),max(LowPress),max(AverTemper),max(HighTemper),max(LowTemper),max(AverSPress) from data;")
        results = list(cur.fetchall())

        for r in results[0]:
            result_list.append(('%s' % r))

        for r in result_list:
            re = int(r)
            result.append(re)
    elif type == "min":
        Count = cur.execute(
            "select min(AverPress),min(HighPress),min(LowPress),min(AverTemper),min(HighTemper),min(LowTemper),min(AverSPress) from data;")
        results = list(cur.fetchall())

        for r in results[0]:
            result_list.append(('%s' % r))

        for r in result_list:
            re = int(r)
            result.append(re)
    else:
        pass

    cur.close()
    conn.close()
    return result

if __name__ == '__main__':
    result = Weather_Similar("", "max")
    print(result)
    result = Weather_Similar("", "min")
    print(result)
    result = Weather_Similar()
    print(result)