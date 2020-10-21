# flow control

#x = int(input('Please enter an integer :'))
x = 0

if x < 0:
    x = 0
    print('Negative changed to Zero')
elif x == 0:
    print("Zero")
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat' , 'window' , 'defenestrate']
for w in words:
    print(w , len(w))

for w in words[1:]:
    if len(w) > 6:
        words.insert(0,w)
        words.append(w)
        words.remove(w)
print(words)

for i in range(5):
    print(i)
for i in range(5,4):
    print(i)
for i in range(5,100,20):
    print(i)

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i]);

for i , season in enumerate(['春','夏','秋','冬']):
    print(i,season)

print(range(10))

print(list(range(5)))
print(list([0, 1, 2, 3, 4]))
l = list(range(5))
print(l)

for n in range(2, 15):
    for x in range(2, n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break;
    else:# The ELSE is in the for loop.
        print(n,'is a prime number')


for num in range(1, 10):
    if num % 2 == 0:
        print('Found an even number',num)
        continue
    print("Found an odd number",num)

while True:#nothing to do
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass