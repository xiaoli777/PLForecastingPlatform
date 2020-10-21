import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# 读取自带的diabete数据集
diabetes = datasets.load_diabetes()


# 使用其中的一个feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# 将数据集分割成training set和test set
diabetes_X_train = np.mat([[313.0, -10030.0, 304.0, 280.0, 354.0, -10006.0, -10043.0], [312.0, -10039.0, 314.0, 281.0, 359.0, -10018.0, -10055.0], [279.0, -10000.0, 310.0, 262.0, 323.0, -9977.0, -10012.0], [283.0, -10014.0, 308.0, 263.0, 321.0, -9997.0, -10027.0], [270.0, -10031.0, 296.0, 253.0, 286.0, -10017.0, -10041.0]])
diabetes_X_test = np.mat([[286.0, -10035.0, 303.0, 263.0, 333.0, -10013.0, -10049.0],])

# 将目标（y值）分割成training set和test set
diabetes_y_train = np.mat([[8376.66], [8001.37], [8229.48], [8004.41], [6379.17]])
diabetes_y_test = np.mat([[8004.41]])

# 使用线性回归
regr = linear_model.LinearRegression()

# 进行training set和test set的fit，即是训练的过程
regr.fit(diabetes_X_train, diabetes_y_train)

print(regr.predict(diabetes_X_test))

"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# 读取自带的diabete数据集
diabetes = datasets.load_diabetes()


# 使用其中的一个feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# 将数据集分割成training set和test set
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 将目标（y值）分割成training set和test set
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# 使用线性回归
regr = linear_model.LinearRegression()

# 进行training set和test set的fit，即是训练的过程
regr.fit(diabetes_X_train, diabetes_y_train)

# 打印出相关系数和截距等信息
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# 使用pyplot画图
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
"""