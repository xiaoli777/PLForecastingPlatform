#Structure
a = [66.24, 333, 333, 1, 1234.5]
print(a.count(333), a.count(1), a.count('x'))
a.insert(2, -1)
a.append(333) #a.insert(len(a), 333);a[len(a):] = 333
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
a.reverse()
print(a)
print(a.pop(0))
print(a.pop())
a.extend(a)
print(a)
a.clear()
print(a)

#Stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

#Queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.pop())
print(queue)

#List Expression
squares1 = list(map(lambda x : x**2, range(10)))
print(squares1)
squares2 = [x**2 for x in range(10)]
print(squares2)

points = [(x**2, y**2) for x in range(5) for y in range(5) if x != y if x > y]
print(points)

fruit = ("banana", "apple", "pear")
weapons = [(weapon.strip(), weapon.strip()) for weapon in fruit]
print(weapons)

vec = [(1, 2, 3), (4, 5), (6, 7, 8)]
vecX = [num for elem in vec for num in elem]
print(vecX)

from math import pi
print([str(round(pi, x)) for x in range(1,6)])

#Nested List Expression
Matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(len(Matrix[0]))
print([[row[i] for row in Matrix] for i in range(4)])
transposed = []
# for i in range(4)
#     transposed.append([row[i] for row in Matrix])
print([row[i] for i in range(4) for row in Matrix])
print(list(zip(*Matrix)))
print(Matrix)

#Del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
# print(a)