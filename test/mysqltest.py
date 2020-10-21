import pymysql

date_start = "2005-1-1"
date_end = "2005-12-31"
paramter = 1

conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='pl') #db：库名
cur = conn.cursor()

date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"
season = " and season = (select season from datasetH where date = '" + date_end + "')"
holiday = " and holiday = (select holiday from datasetH where date = '" + date_end + "')"
finish_signal = ";"

if paramter == 1:
    season = ""
    holiday = ""
elif paramter == 3:
    holiday = ""
elif paramter == 5:
    season = ""
else:
    pass

print(holiday)
print(season)
AverTemperlist = []
AverTemper = []

Count = cur.execute('select date from datasetH' + date_during + season + holiday + finish_signal)
results = cur.fetchall()
result = list(results)
for r in result:
    AverTemperlist.append(('%s' % r))

# for pl in AverTemperlist:
#     pl = int(pl)
#     AverTemper.append(pl)

# print(AverTemper)
print(result)

conn.commit()
cur.close()
conn.close()

print(Count)