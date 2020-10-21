a , b = 0 , 1
while b < 10:
    print(b)
    a , b = b , a + b
print("end")

i = 256 * 256
print('The value of i is', i);

a , b = 0 , 1
while b < 1000:
    print(b , end = '!')
    a ,b = b , a + b

import numpy as np

# print(np.random.random((3,4)))
# print(np.random.rand((3,4)))

x1 = [1,2]
x2 = [3,4]
x = np.mat([x1,x2])
print(x)
print(x**2)

# f=open("NetWorkOUT.txt","w+")
#
# networkout2 = [[1,2,3,4]]
# for i in networkout2[0]:
#     f.writelines(str(i)+'\n')
#
# f.close()

Year = 1900
Feb = 28
if Year % 400 == 0 or Year % 4 == 0 and Year % 100 != 0:
    Feb = 29
print(Feb)

a = [0,]
b = [1,2]
c = a + b
d = c[1:9]
print(d)

from numpy import *

e = [[1,2],[3,4],[5,6],[7,8],[9,10],[6,7],[8,8]]
f = mat(e)
print(f[0:2, : ])
print(f[5, : ])
print(f.shape[0])
print(mat(ones((f.shape[0], 1))))
print(mat(zeros((f.shape[0], 2))))
a = [[1],[2],[3],[4],[5]]
print(mat(a).shape[0])
print(multiply(a,a))

# from PIL import Image
# import matplotlib.pyplot as plt
# img=Image.open('simulation.png')
# img.show()
#
# img1=Image.open('simulation.png')
# plt.figure("dog1")
# plt.imshow(img1)
# plt.show()

myList = [1, 2, 3, 3, 2, 2, 4, 5, 5]
print(myList)
[1, 2, 3, 3, 2, 2, 4, 5, 5]
myList = list(set(myList))
print(myList)
[1, 2, 3, 4, 5]

def func(list):
    #list.clear()
    list.append(2)
    list.append(6)

Lis = [1,2,3]
print(Lis)
func(Lis)
print(Lis)

