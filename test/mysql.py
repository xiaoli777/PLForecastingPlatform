import pymysql

#连接数据库
conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='test') #db：库名
#创建游标 默认为元组形式
cur = conn.cursor()
#cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

#创建table
#reCount = cur.execute('create table tab1(num char(5) primary key, name char(10), age int(4));')

#查询数据 and 打印数据
reCount = cur.execute('select * from mytab;')
#fetchall:获取lcj表中所有的数据
ret1 = cur.fetchall()
print(ret1)
print("----------------------")
# 相对当前位置移动【1：表示向下移动一行，-1：表示向上移动一行】 超过范围会溢出
cur.scroll(-1,mode='relative')
# 相对绝对位置移动 【1：表示向上移动一行，-1：表示向下移动一行，0：表示到起始位置】
cur.scroll(0,mode='absolute')
#获取lcj表中前三行数据
ret2 = cur.fetchmany(3)
print(ret2)
print("------------------------------")
#获取lcj表中第一行数据
ret3= cur.fetchone()
print(ret3)

#向test库中的lcj表插入
# reCount = cur.executemany("insert into mytab(num,name,age,info) "
#                           "values (%s,%s,%s,%s);", [(4,"whc",23,'VVVG'),(5,'lr',24,'VVVVG')]);

#提交
conn.commit()
#关闭指针对象
cur.close()
#关闭连接对象
conn.close()

#打印结果 create:0表正确 select:表结果数量
print(reCount)