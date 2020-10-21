import pymysql

conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='powerload') #db：库名
cur = conn.cursor()

#Count = cur.execute('insert into Data(Date,AverPress,HighPress,LowPress,AverTemper,HighTemper,LowTemper,AverSPress,PowerLoadAver,PowerLoadMax,PowerLoadMin)'
#                    ' values ("2008-1-1",1,1,1,1,1,1,1,1,1,1) on duplicate key'
#                    ' update AverPress = 2,HighPress = HighPress + 1;')

#Count = cur.execute('select PowerLoadMax from data where date >= DATE_SUB("2007-1-1",INTERVAL 7 DAY) and date < "2007-1-1";')
Count = cur.execute('select date from data where date = DATE_SUB("2007-1-1",INTERVAL 7 DAY);')
TempList = []
results = cur.fetchall()
result = list(results)
for r in result:
    TempList.append(('%s' % r))
print(TempList)
print(Count)

conn.commit()
cur.close()
conn.close()

