import pymysql

def Cal_History(name, start = '2005-1-1' ,end = '2005-1-31'):
    result_list = []
    result = []
    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload', charset='utf8')
    cur = conn.cursor()

    Count = cur.execute("select " + name + " from data where date between '" + start + "' and '" + end + "';")
    results = list(cur.fetchall())

    for r in results:
        result_list.append(('%s' % r))

    if name == "date":
        return result_list

    for r in result_list:
        re = float(r)
        result.append(re)

    cur.close()
    conn.close()
    return result

if __name__ == '__main__':
    result = Cal_History("AverTemper")
    print(result)