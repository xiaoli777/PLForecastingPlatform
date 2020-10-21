import numpy as np
import matplotlib.pyplot as plt

def logsig(x):
    return 1/(1+np.exp(-x))

AverTemper = [66,87,117,134,141,150,166,160,128,124,136,119,74,86,94,114,120,161,154,134]
AverPress = [10245,10195,10153,10174,10178,10167,10168,10176,10189,10185,10182,10183,10179,10185,10182,10185,10173,10157,10169,10211]
AverSPress = [34,39,68,96,84,104,116,93,79,79,90,80,85,60,46,50,75,106,99,100]
LowTemper = [21,70,75,118,125,122,115,117,90,84,103,107,64,49,50,74,75,120,129,120]
HighTemper = [114,124,114,165,167,222,227,214,174,184,180,140,107,144,160,176,187,216,183,151]
LowPress = [10205,10158,10137,10157,10160,10140,10149,10153,10167,10157,10166,10156,10161,10155,10156,10154,10143,10131,10149,10181]
HighPress = [10283,10277,10172,10197,10202,10194,10198,10209,10222,10216,10203,10313,10198,10219,10208,10215,10200,10183,10190,10236]

PowerLoadMax = [3993.32,4509.39,4650.00,4729.59,4491.29,
                4315.92,4339.53,4559.79,4501.38,4608.76,
                4430.12,4579.43,4509.40,4433.88,4487.50,
                4498.39,4621.70,4650.96,4472.82,4425.38]

samplein = np.mat([AverTemper,AverPress,AverSPress,LowTemper,HighTemper,LowPress,HighPress])
sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0],samplein.max(axis=1).T.tolist()[0]]).transpose()
#print(sampleinminmax)
sampleout = np.mat([PowerLoadMax])   #二维数组
sampleoutminmax = np.array([sampleout.min(axis=1).T.tolist()[0],sampleout.max(axis=1).T.tolist()[0]]).transpose()
#print(sampleoutminmax)

sampleinnorm = (2*(np.array(samplein.T)-sampleinminmax.transpose()[0])/(sampleinminmax.transpose()[1]-sampleinminmax.transpose()[0])-1).transpose()
sampleoutnorm = (2*(np.array(sampleout.T).astype(float)-sampleoutminmax.transpose()[0])/(sampleoutminmax.transpose()[1]-sampleoutminmax.transpose()[0])-1).transpose()

noise = 0.03*np.random.rand(sampleoutnorm.shape[0],sampleoutnorm.shape[1])
sampleoutnorm += noise

maxepochs = 70000
learnrate = 0.035
errorfinal = 0.1*10**(-2)
samnum = 20
indim = 7
outdim = 1
hiddenunitnum = 10

w1 = 0.5*np.random.rand(hiddenunitnum,indim)-0.1
b1 = 0.5*np.random.rand(hiddenunitnum,1)-0.1
w2 = 0.5*np.random.rand(outdim,hiddenunitnum)-0.1
b2 = 0.5*np.random.rand(outdim,1)-0.1

errhistory = []

for i in range(maxepochs):
    hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
    networkout = (np.dot(w2, hiddenout).transpose() + b2.transpose()).transpose()
    # networkout = logsig((np.dot(w2,hiddenout).transpose()+b2.transpose())).transpose()
    err = sampleoutnorm - networkout
    sse = sum(sum(err**2))
    # if i%100 == 0:
    #     print(err**2)
    #     print(sum(err**2))
    #     print(sum(sum(err**2)))
    if i <= 100:
        print(err ** 2)
        print(sum(err**2))
        print(sum(sum(err**2)))

    errhistory.append(sse)
    if sse < errorfinal:
        break

    delta2 = err
    # delta2 = err*networkout*(1-networkout)

    delta1 = np.dot(w2.transpose(),delta2)*hiddenout*(1-hiddenout)

    dw2 = np.dot(delta2,hiddenout.transpose())
    db2 = np.dot(delta2,np.ones((samnum,1)))

    dw1 = np.dot(delta1,sampleinnorm.transpose())
    db1 = np.dot(delta1,np.ones((samnum,1)))

    w2 += learnrate*dw2
    b2 += learnrate*db2

    w1 += learnrate*dw1
    b1 += learnrate*db1

# 误差曲线图
errhistory10 = np.log10(errhistory)
minerr = min(errhistory10)
plt.plot(errhistory10)
plt.plot(range(0,i+1000,1000),[minerr]*len(range(0,i+1000,1000)))

ax=plt.gca()
ax.set_yticks([-2,-1,0,1,2,minerr])
ax.set_yticklabels([u'$10^{-2}$',u'$10^{-1}$',u'$1$',u'$10^{1}$',u'$10^{2}$',str(('%.4f'%np.power(10,minerr)))])
ax.set_xlabel('iteration')
ax.set_ylabel('error')
ax.set_title('Error History')
plt.savefig('PLerrorhistory.png',dpi=700)
plt.close()

# 仿真输出和实际输出对比图
hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
diff = sampleoutminmax[:,1]-sampleoutminmax[:,0]
networkout2 = (networkout+1)/2   #与之前的-1以及*2相互对应
# networkout2 = networkout
networkout2[0] = networkout2[0]*diff[0]+sampleoutminmax[0][0]

sampleout = np.array(sampleout)   #real value

ax=plt.gca()
line1, = ax.plot(networkout2[0] - 4000,'k',marker = u'$\circ$')
line2, = ax.plot(sampleout[0] - 4000,'r',markeredgecolor='b',marker = u'$\star$',markersize=9)

ax.legend((line1,line2),('simulation output','real output'),loc = 'upper left')

yticks = [-100,0,100,200,300,400,500,600,700,800,900]
ytickslabel = [u'$-100$',u'$0$',u'$100$',u'$200$',u'$300$',u'$400$',u'$500$',u'$600$',u'$700$',u'$800$',u'$900$']
ax.set_yticks(yticks)
ax.set_yticklabels(ytickslabel)
ax.set_ylabel(u'Power Load$(+4000)$')

xticks = range(0,20,2)
xtickslabel = range(0,20,2)
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabel)
ax.set_xlabel(u'Day')
ax.set_title('Power Load Simulation')

plt.savefig('PLsimulation.png',dpi=500,bbox_inches='tight')
plt.close()

# print(sampleout[0])
# print(sampleoutminmax[:,1],sampleoutminmax[:,0],sampleoutminmax[0][0])
# print(networkout2[0])