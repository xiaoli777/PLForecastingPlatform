#output
s = 'hello, world'
print(repr(s))
print(str(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = " ")   # str.ljust()   str.center()   cut:str.ljust(n)[:n]
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('The story of {0},{1},and {other}.'.format('bill','manfred',other='georg'))

f = open('workfile','r+')
print(f.read(2))
print(f.read(3))
#print(f.read())

print(f.readline())

for line in f:
    print(line,end = "!")

print(list(f))

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
print(s)
print(f.write(s))
f.close()

f1 = open('workfile1', 'rb+') #binary
print(f1.write(b'0123456789abcdef'))
print(f1.seek(5))   # infornt +5
print(f1.read(1))
print(f1.tell())
print(f1.seek(-3, 2))   # behind -3
print(f1.read(1))
print(f1.tell())
f1.close()

with open('workfile', 'r') as f:  #aotu closure
    f.readline()
print(f.closed)