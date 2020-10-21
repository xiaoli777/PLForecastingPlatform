import pymysql

class Weather:
    def __init__(self, date = [], AverSPress =[], LowTemper = [], HighTemper = [], AverTemper =[], LowPress = [], HighPress = [], AverPress =[]):
        self.date = date
        self.AverSPress = AverSPress
        self.LowTemper = LowTemper
        self.HighTemper = HighTemper
        self.AverTemper = AverTemper
        self.LowPress = LowPress
        self.HighPress = HighPress
        self.AverPress = AverPress

def weather_search(item,start,end):
    TempList = []
    Temp = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    Count = cur.execute('select ' + item + ' from data where date >= "'
                        + start + '" and date <= "' + end + '";')

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

    return Temp

def Weather_Main(start = '2005-1-1',end = '2005-1-1'):
    DateList = []

    conn = pymysql.connect(host='localhost', port=3306, user='yxl', passwd='123456', db='powerload')  # db：库名
    cur = conn.cursor()

    Count = cur.execute('select date from data where date >= "'
                        + start + '" and date <= "' + end + '";')

    results = cur.fetchall()
    result = list(results)

    for r in result:
        DateList.append(('%s' % r))

    cur.close()
    conn.close()

    AverSPress = weather_search('AverSPress',start,end)
    LowTemper = weather_search('LowTemper',start,end)
    HighTemper = weather_search('HighTemper',start,end)
    AverTemper = weather_search('AverTemper',start,end)
    LowPress = weather_search('LowPress',start,end)
    HighPress = weather_search('HighPress',start,end)
    AverPress = weather_search('AverPress',start,end)
    return Weather(DateList,AverSPress,LowTemper,HighTemper,AverTemper,LowPress,HighPress,AverPress)

if __name__ == '__main__':
    Result = Weather_Main()
    print(Result.date)
    print(Result.AverSPress)
    print(Result.LowTemper)
    print(Result.HighTemper)
    print(Result.AverTemper)
    print(Result.LowPress)
    print(Result.HighPress)
    print(Result.AverPress)

