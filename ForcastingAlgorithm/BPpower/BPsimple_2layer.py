import numpy as np

#No hiddenunit
# sigmoid function 机智，一个函数当作两个用
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1    #hiddenunitnum = 1
print(syn0)

for iter in range(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?只有输入层到隐层的权值修正。。。。
    l1_error = y - l1

    # if iter%100 != 0:
    #     print(l1_error)

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)   #关键步骤、logsig图的斜率在于(0,1)之间

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
print("Output After Training:")
print(l1)