import time
import datetime

startTime= time.strftime("%Y-%m-%d %H:%M:%s", time.localtime())
endTime= time.strftime("%Y-%m-%d %H:%M:%s", time.localtime())
startTime= datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
endTime= datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
# 相减得到秒数
seconds = (endTime- startTime).seconds
hours=(endTime- startTime).hours
day=(endTime- startTime).day