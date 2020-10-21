import pymysql

def impFile(fileName):
    Date = []
    AverPress = []
    HighPress = []
    LowPress = []
    AverTemper = []
    HighTemper = []
    LowTemper = []
    AverSPress = []
    PowerLoadAver = []
    PowerLoadMax = []
    PowerLoadMin = []

    f = open(fileName, "r")
    for line in f.readlines():
        lineArr = line.strip().split('\t')
        Date.append(str(lineArr[0]))
        AverPress.append(str(lineArr[1]))
        HighPress.append(str(lineArr[2]))
        LowPress.append(str(lineArr[3]))
        AverTemper.append(str(lineArr[4]))
        HighTemper.append(str(lineArr[5]))
        LowTemper.append(str(lineArr[6]))
        AverSPress.append(str(lineArr[7]))
        PowerLoadAver.append(str(lineArr[8]))
        PowerLoadMax.append(str(lineArr[9]))
        PowerLoadMin.append(str(lineArr[10]))
    f.close()

    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload') #db：库名
    cur = conn.cursor()

    for i in range(1,len(Date),1):
        # print('insert into Data(' + Date[0] + ',' + AverPress[0] + ',' + HighPress[0] + ',' +
        #       LowPress[0] + ',' + AverTemper[0] + ',' + HighTemper[0] + ',' + LowTemper[0] + ',' +
        #       AverSPress[0] + ',' + PowerLoadAver[0] + ',' + PowerLoadMax[0] + ',' + PowerLoadMin[0] + ')' +
        #       ' values ("' + Date[i] + '",' + AverPress[i] + ',' + HighPress[i] + ',' + LowPress[i] + ',' +
        #       AverTemper[i] + ',' + HighTemper[i] + ',' + LowTemper[i] + ',' + AverSPress[i] +
        #       ',' + PowerLoadAver[i] + ',' + PowerLoadMax[i] + ',' + PowerLoadMin[i] + ') on duplicate key update ' +
        #       AverPress[0] + '=' + AverPress[i] + ',' + HighPress[0] + '=' + HighPress[i] + ',' +
        #       LowPress[0] + '=' + LowPress[i] + ',' + AverTemper[0] + '=' + AverTemper[i] + ',' +
        #       HighTemper[0] + '=' + HighTemper[i] + ',' + LowTemper[0] + '=' + LowTemper[i] + ',' +
        #       LowPress[0] + '=' + LowPress[i] + ',' + AverTemper[0] + '=' + AverTemper[i] + ',' +
        #       AverSPress[0] + '=' + AverSPress[i] + ',' + PowerLoadAver[0] + '=' + PowerLoadAver[i] + ',' +
        #       PowerLoadMax[0] + '=' + PowerLoadMax[i] + ',' + PowerLoadMin[0] + '=' + PowerLoadMin[i] + ';')

        Count = cur.execute('insert into Data(' + Date[0] + ',' + AverPress[0] + ',' + HighPress[0] + ',' +
                        LowPress[0] + ',' + AverTemper[0] + ',' + HighTemper[0] + ',' + LowTemper[0] + ',' +
                        AverSPress[0] + ',' + PowerLoadAver[0] + ',' + PowerLoadMax[0] + ',' + PowerLoadMin[0] + ')' +
                        ' values ("' + Date[i] + '",' + AverPress[i] + ',' + HighPress[i] + ',' + LowPress[i] + ',' +
                        AverTemper[i] + ',' + HighTemper[i] + ',' + LowTemper[i] + ',' + AverSPress[i] +
                        ',' + PowerLoadAver[i] + ',' + PowerLoadMax[i] + ',' + PowerLoadMin[i] + ') on duplicate key update ' +
                        AverPress[0] + '=' + AverPress[i] + ',' + HighPress[0] + '=' + HighPress[i] + ',' +
                        LowPress[0] + '=' + LowPress[i] + ',' + AverTemper[0] + '=' + AverTemper[i] + ',' +
                        HighTemper[0] + '=' + HighTemper[i] + ',' + LowTemper[0] + '=' + LowTemper[i] + ',' +
                        LowPress[0] + '=' + LowPress[i] + ',' + AverTemper[0] + '=' + AverTemper[i] + ',' +
                        AverSPress[0] + '=' + AverSPress[i] + ',' + PowerLoadAver[0] + '=' + PowerLoadAver[i] + ',' +
                        PowerLoadMax[0] + '=' + PowerLoadMax[i] + ',' + PowerLoadMin[0] + '=' + PowerLoadMin[i] + ';')

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    impFile("D:/Work/Eric6Save/PowerLoadPredict/SAVE/DataSetNew2008.txt")