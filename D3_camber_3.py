# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pandas import DataFrame


def draw(x, y, z):
    '''
    采用matplolib绘制曲面图
    :param x: x轴坐标数组
    :param y: y轴坐标数组
    :param z: z轴坐标数组
    :return:
    '''
    X = x
    Y = y
    Z = z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(X, Y, Z)
    plt.show()


if __name__ == '__main__':
    '''
       默认执行方式：
             1.获取当前文件夹下的1.log文件
             2.将数据格式化为矩阵
             3.以矩阵的列索引为x坐标，行索引为y坐标，值为z坐标
             4.绘制曲面图
    '''
    data = {}
    index_origin = 0
    f = open("1.log")
    line = f.readline()
    while line:
        data[index_origin] = line.split('=')[-1].replace(' ', '').split('f,')[0:-1]
        index_origin = index_origin + 1
        line = f.readline()
    f.close()
    df = DataFrame(data)
    df = df.T

    x = []
    for i in range(len(df.index)):
        x = x + list(df.columns)
    print(x)

    y = []
    for i in range(len(df.index)):
        for m in range(17):
            y.append(i)
    print(y)

    z = []
    for i in range(len(df.index)):
        z = z + df[i:i + 1].values.tolist()[0]
    z = map(float, z)
    print(z)
    draw(x, y, z)