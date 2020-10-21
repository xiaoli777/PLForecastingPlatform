#Tuple unchangble
t = 12345, 54321, 'hello',
r = (12345, 54321, 'hello')
s = [12345, 54321, 'hello']
if t == r:
    print("1")
if s == t:
    print("2")
print(t)
print(r)
print(s)

u = t, (1, 2, 3, 4, 5)
print(u)
print(u[1])

empty = ()
singleton_1 = 'hello',
singleton_2 = ('hello', "ha",)
print(singleton_1, singleton_2)

x, y, z = t
print(x, y, z)

#set no repetition
emptyset = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(emptyset, basket)
print('orange' in basket)
print('dog' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(b - a)
print(a | b)
print(a & b)
print(a ^ b)
print((a - b) | (b - a))

c = {x for x in a if x not in b}
print(c)
print(x)   # what's mean

#dictionary unchangble
emptydic = {}
tel = {'jack' : 4098, 'sape' : 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['jack']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(tel.keys()) #view
print(sorted(tel.keys()))
print('jack' in tel)
print('guido' in tel)

dic_1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dic_2 = {x: x**2 for x in (2, 4, 6)}
dic_3 = {x: x**2 for x in [2, 4, 6]}
dic_4 = dict([(x, x**2) for x in [2, 4, 6]])
dic_5 = dict(sape = 4139, guido = 4127, jack = 4098)
print(dic_1, dic_2, dic_3, dic_4, dic_5)

#loop trick
knights = {'gallahad' : 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ('lancelot', 'the holy grail', 'blue')
for a, q in zip(answers, questions):
    print('What is your {0}?It is {1}'.format(q, a))
    print('What is your', q, '?It is', a)

for i in reversed(range(1, 10, 2)):
    print(i)

for f in sorted(set(basket)):
    print(f, end='!')

print('\nNew line')
for d in sorted(tel.keys()):
    print(d, end='!')
print(d)

words = ['cat', 'window', 'defenestrate']
wordscopy_1 = words.copy()
wordscopy_2 = words
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)
print(wordscopy_1)
print(wordscopy_2)
if words is wordscopy_2:
    print("Shallow copy")

temp = 1
if temp is 1:
    print("is")
if temp is not 2:
    print('is not')
if temp == 1:
    print('==')
if temp != 2:
    print('!=')

if 9 > temp == 1:
    print("true")
if 9 > temp < 7:
    print("true")

#not > and > or(and\or is shortcut)
if temp is 2 and not 3 or 1:
    print("turth")

if temp == 0 or 1 and 1:#only true or false!Noelse
    print("true")
else:
    print("false")
print(0 or 1 and 1)

t1 = [1, 2, 3, 4]
t2 = [1, 2, 3, 4]
print(t1 == t2)
print(t1 is [1, 2, 3, 4])
print(t1 is t2)
print(id(t1))
print(id(t2))

str1, str2, str3 = '', 'Tron', 'Hammer'
non_null_1 = str1 or str2 or str3
non_null_2 = str1 and str2 and str3
print(non_null_1,non_null_2)

#comparison
print("1、", (1, 2, 3) < (1, 2, 4))
print("2、", [1, 2, 3] < [1, 2, 4])
print("3、", {1, 2, 3} == {1, 3, 2})
print("4、", [1, 2, 3] == [1, 3, 2])
print("5、", 'ABC' < 'C' < 'Pascal' < 'Python')
print("6、", (1, 2, 3, 4) < (1, 2, 4))
print("7、", (1, 2) < (1, 2, -1))
print("8、", (1, 2, 3) == (1.0, 2.0, 3.0))
print("9、", (1, 2, ('aa', 'bb')) < (1, 2, ('abc', 'a'), 4))
print("10、", [1, 2, 3] == {1, 2, 3})
#print("11、", [1, 2, 3] > {1, 2, 3}) #TypeError
