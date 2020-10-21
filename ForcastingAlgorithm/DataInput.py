import pymysql

conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='PL')
cur = conn.cursor()

PowerLoadMAXlist = []
PowerLoadMAX = []

Count = cur.execute('select PowerLoadMax from dataset2005;')
results = cur.fetchall()
result = list(results)
for r in result:
    PowerLoadMAXlist.append(('%.2f' % r))

for pl in PowerLoadMAXlist:
    pl = float(pl)
    PowerLoadMAX.append(pl)

#游标归零，默认mode='relative'
cur.scroll(0,mode='absolute')

print(PowerLoadMAXlist)
print(PowerLoadMAX)
print(Count)

conn.commit()
cur.close()
conn.close()