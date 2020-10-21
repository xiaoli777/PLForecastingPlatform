import numpy as np
import pymysql
import matplotlib.pyplot as plt

def logsig(x):
    return 1/(1+np.exp(-x))

def func(project_name = "NetWorkOUT", date_start = "2005-01-01", date_end = "2005-01-01", paramter = 1):
    conn = pymysql.connect(host='localhost',port= 3306,user = 'yxl',passwd='123456',db='PL')
    cur = conn.cursor()

    date_during = " where date >= '" + date_start + "' and date <= '" + date_end + "'"
    season = " and season = (select season from datasetH where date = '" + date_end + "')"
    holiday = " and holiday = (select holiday from datasetH where date = '" + date_end + "')"
    finish_signal = ";"

    if paramter == 1:
        season = ""
        holiday = ""
    elif paramter == 5:
        holiday = ""
    elif paramter == 3:
        season = ""
    else:
        pass

    AverTemperlist = []
    AverPresslist = []
    AverSPresslist = []
    LowTemperlist = []
    HighTemperlist = []
    LowPresslist = []
    HighPresslist = []
    PowerLoadMaxlist = []
    DateSelectedlist = []
    AverTemper = []
    AverPress = []
    AverSPress = []
    LowTemper = []
    HighTemper = []
    LowPress = []
    HighPress = []
    PowerLoadMax = []
    DateSelected = []

    #日平均气温读取
    Count = cur.execute('select AverTemper from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        AverTemperlist.append(('%s' %r))

    for pl in AverTemperlist:
        pl = int(pl)
        AverTemper.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日平均气压读取
    Count = cur.execute('select AverPress from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        AverPresslist.append(('%s' % r))

    for pl in AverPresslist:
        pl = int(pl)
        AverPress.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日平均水汽压读取
    Count = cur.execute('select AverSPress from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        AverSPresslist.append(('%s' % r))

    for pl in AverSPresslist:
        pl = int(pl)
        AverSPress.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日最低温度读取
    Count = cur.execute('select LowTemper from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        LowTemperlist.append(('%s' % r))

    for pl in LowTemperlist:
        pl = int(pl)
        LowTemper.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日最高温度读取
    Count = cur.execute('select HighTemper from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        HighTemperlist.append(('%s' % r))

    for pl in HighTemperlist:
        pl = int(pl)
        HighTemper.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日最低气压读取
    Count = cur.execute('select LowPress from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        LowPresslist.append(('%s' % r))

    for pl in LowPresslist:
        pl = int(pl)
        LowPress.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日最高气压读取
    Count = cur.execute('select HighPress from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        HighPresslist.append(('%s' % r))

    for pl in HighPresslist:
        pl = int(pl)
        HighPress.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 日最大负荷读取
    Count = cur.execute('select PowerLoadMax from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        PowerLoadMaxlist.append(('%.2f' % r))

    for pl in PowerLoadMaxlist:
        pl = float(pl)
        PowerLoadMax.append(pl)

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    # 选择日期读取
    Count = cur.execute('select Date from datasetH' + date_during + season + holiday + finish_signal)
    results = cur.fetchall()
    result = list(results)
    for r in result:
        DateSelectedlist.append(('%s' % r))

    #游标归零，默认mode='relative'
    cur.scroll(0,mode='absolute')

    #print(DateSelected)
    
    low,  high = 0, Count
    if Count > 31:
        low , high = Count - 31, Count
    AverTemper = AverTemper[low:high]
    AverPress = AverPress[low:high]
    AverSPress = AverSPress[low:high]
    LowTemper = LowTemper[low:high]
    HighTemper = HighTemper[low:high]
    LowPress = LowPress[low:high]
    HighPress = HighPress[low:high]
    PowerLoadMax = PowerLoadMax[low:high]
    DateSelectedlist = DateSelectedlist[low:high]
    
    #print(DateSelected)
    index = 0
    for pl in DateSelectedlist:
        if Count >= 10:
            if index % 3 == 0:
                pl = pl[5:]
            else:
                pl = ""
            index = index + 1
        else:
            pl = pl[5:]
        DateSelected.append(pl)
    #print(DateSelected)
    
    # print(AverTemper)
    # print(AverPress)
    # print(AverSPress)
    # print(LowTemper)
    # print(HighTemper)
    # print(LowPress)
    # print(HighPress)
    # print(PowerLoadMax)
    # print(Count)

    # conn.commit()
    cur.close()
    conn.close()

    samplein = np.mat([AverTemper,AverPress,AverSPress,LowTemper,HighTemper,LowPress,HighPress])
    sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0],samplein.max(axis=1).T.tolist()[0]]).transpose()
    sampleout = np.mat([PowerLoadMax])
    sampleoutminmax = np.array([sampleout.min(axis=1).T.tolist()[0],sampleout.max(axis=1).T.tolist()[0]]).transpose()

    sampleinnorm = (2*(np.array(samplein.T)-sampleinminmax.transpose()[0])/(sampleinminmax.transpose()[1]-sampleinminmax.transpose()[0])-1).transpose()
    sampleoutnorm = (2*(np.array(sampleout.T).astype(float)-sampleoutminmax.transpose()[0])/(sampleoutminmax.transpose()[1]-sampleoutminmax.transpose()[0])-1).transpose()

    noise = 0.03*np.random.rand(sampleoutnorm.shape[0],sampleoutnorm.shape[1])
    sampleoutnorm += noise

    maxepochs = 60000
    learnrate = 0.035
    errorfinal = 0.1*10**(-2)
    samnum = high - low
    indim = 7
    outdim = 1
    hiddenunitnum = 10

    w1 = 0.5*np.random.rand(hiddenunitnum,indim)-0.1
    b1 = 0.5*np.random.rand(hiddenunitnum,1)-0.1
    w2 = 0.5*np.random.rand(outdim,hiddenunitnum)-0.1
    b2 = 0.5*np.random.rand(outdim,1)-0.1

    errhistory = []

    #print(PowerLoadMax)

    for i in range(maxepochs):
        hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
        networkout = (np.dot(w2, hiddenout).transpose() + b2.transpose()).transpose()
        err = sampleoutnorm - networkout
        # if i <= 3:
        #     print(err)
        sse = sum(sum(err**2))

        errhistory.append(sse)
        if sse < errorfinal:
            break

        delta2 = err

        delta1 = np.dot(w2.transpose(), delta2) * hiddenout * (1 - hiddenout)

        dw2 = np.dot(delta2, hiddenout.transpose())
        db2 = np.dot(delta2, np.ones((samnum, 1)))

        dw1 = np.dot(delta1, sampleinnorm.transpose())
        db1 = np.dot(delta1, np.ones((samnum, 1)))

        w2 += learnrate * dw2
        b2 += learnrate * db2

        w1 += learnrate * dw1
        b1 += learnrate * db1

    # 误差曲线图
    errhistory10 = np.log10(errhistory)
    minerr = min(errhistory10)
    plt.plot(errhistory10)
    plt.plot(range(0,i+1000,1000),[minerr]*len(range(0,i+1000,1000)))

    ax=plt.gca()
    ax.set_yticks([-2,-1,0,1,2,minerr])
    ax.set_yticklabels([u'$10^{-2}$',u'$10^{-1}$',u'$1$',u'$10^{1}$',u'$10^{2}$',str((''%np.power(10,minerr)))])
    ax.set_xlabel('iteration')
    ax.set_ylabel('error')
    ax.set_title('Error History')
    plt.savefig('SAVE\\' + project_name + ' PLerrorhistory.png',dpi=100)
    plt.close()

    # 仿真输出和实际输出对比图
    hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
    networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
    diff = sampleoutminmax[:,1]-sampleoutminmax[:,0]
    networkout2 = (networkout+1)/2
    networkout2[0] = networkout2[0]*diff[0]+sampleoutminmax[0][0]

    sampleout = np.array(sampleout)   #real value

    #print(sampleout[0],networkout2[0])

    plt.figure(project_name + '电力负荷预测分析')
    ax=plt.gca()
    line1, = ax.plot(networkout2[0],'k',marker = u'$\circ$')
    line2, = ax.plot(sampleout[0],'r',markeredgecolor='b',marker = u'$\star$',markersize=9)

    ax.legend((line1,line2),('simulation output','real output'),loc = 'upper left')

    yticks = range(0, 10000, 1000)
    ytickslabel = range(0, 10000, 1000)
    ax.set_yticks(yticks)
    ax.set_yticklabels(ytickslabel)
    ax.set_ylabel(u'Power Load')

    xticks = range(0,high - low,1)
    xtickslabel = DateSelected
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabel)
    ax.set_xlabel(u'Date')
    ax.set_title('Power Load Simulation')

    #plt.plot(xticks, yticks)
    plt.ion()
    #plt.style.use('bmh')
    #plt.figure('SAVE\\' + project_name + ' PLsimulation.png')
    #fig.show()
    plt.title(project_name + ' PLsimulation')
    plt.grid(True)
    plt.show()
    plt.savefig('SAVE\\' + project_name + ' PLsimulation.png',dpi=100)
    #plt.close()
    
    f=open("SAVE\\" + project_name + "DateSet.txt","w+")
    for i in range(len(networkout2[0])):
        f.writelines(str(DateSelectedlist[i]) + "\t" + str(sampleout[0][i]) + "\t" + str(networkout2[0][i]) + '\n')
    f.close()
    
class BP(object):
    def __init__(self, project_name, date_start, date_end, paramter):
        self.project_name = project_name
        self.date_start = date_start
        self.date_end = date_end
        self.paramter = paramter

    def BP_test(self):
        func(self.project_name,self.date_start, self.date_end, self.paramter)
