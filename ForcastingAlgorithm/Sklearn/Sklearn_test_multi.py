import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Advertising.csv')

"""散点图"""
# weight = [600,150,200,300,200,100,125,180]
# height = [60,65,73,70,65,58,66,67]
# plt.scatter(height, weight)
# plt.show()

# plt.scatter(data["TV"], data["Radio"])
# plt.title('Wind speed vs fire area')
# plt.xlabel('Wind speed when fire started')
# plt.ylabel('Area consumed by fire')
# plt.show()

"""折线图"""
# age = [5, 10, 15, 20, 25, 30]
# height = [25, 45, 65, 75, 75, 75]
# plt.plot(age, height)
# plt.title('Age vs Height')
# plt.xlabel('age')
# plt.ylabel('Height')
# plt.show()

"""条形图"""
# TV_by_index = data.pivot_table(index="index", values="TV", aggfunc=numpy.sum)
# plt.bar(range(len(TV_by_index)), TV_by_index)
# plt.title('index vs TV')
# plt.xlabel('index')
# plt.ylabel('TV')
# plt.show()

# TV_by_index = data.pivot_table(index="index", values="TV", aggfunc=numpy.sum)
# plt.barh(range(len(TV_by_index)), TV_by_index)
# plt.title('index vs TV')
# plt.xlabel('index')
# plt.ylabel('TV')
# plt.show()

"""主题"""
# plt.style.use('fivethirtyeight')
# plt.plot(data["TV"], data["Radio"])
# plt.show()

# plt.style.use('ggplot')
# plt.plot(data["TV"], data["Radio"])
# plt.show()

recent_grads = pd.read_csv('recent-grads.csv')
#print(recent_grads.head())

"""直方图"""
# recent_grads.hist('Median')
# plt.show()

# recent_grads.hist('Median', bins=20, grid=False)
# plt.show()

# columns = ['Median','Sample_size','Total']
# recent_grads.hist(column=columns, layout=(3,1), grid=False)
# plt.show()

"""箱性图"""
# # 选择两列数据
# sample_size = recent_grads[['Sample_size', 'Major_category']]
# # 按照每一个专业类型分类统计
# sample_size.boxplot(by='Major_category')
# # 将X轴的坐标文字旋转90度，垂直显示
# plt.xticks(rotation=90)
# plt.show()

"""多图合并"""
# plt.scatter(recent_grads['Unemployment_rate'], recent_grads['Median'], color='red')
# plt.scatter(recent_grads['ShareWomen'], recent_grads['Median'], color='blue')
# plt.show()


"""seaborn"""
"""直方图"""
births = pd.read_csv('births.csv')

# sns.distplot(births['births'], kde=True)
# sns.plt.show()

# sns.set_style('dark')                # 该图使用黑色为背景色
# sns.distplot(births['births'], kde=False) # 不显示密度曲线
# plt.xlabel('index')
# plt.ylabel('TV')
# sns.plt.show()

"""箱形图"""
# sns.boxplot(x='year', y='month', data=births)
# sns.plt.show()

# sns.pairplot(births, vars=['year', 'month','births'])
# sns.plt.show()

import numpy as np
import matplotlib.pyplot as plt
plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in range(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()