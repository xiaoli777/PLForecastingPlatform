#List Array
squares = [1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
print(squares + [36,49,64,81,100])

cubes = [1,8,27,65,125] # Changable
cubes[3] = 4 ** 3
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a','b','c','dd','e','f','g']
print(letters)
letters[2:5] = ['C','D','E']
print(letters)
letters[2:5] = []
print(letters)
print(letters[3])
letters[:] = [] # Clear
print(letters)

a = ['a','b','c']
n = ['1','2','3']
x = [['3','2','1'],['c','b','a']]
y = [a,n]
print(x,y)
print(x[1],y[0])
print('x[1][1]',y[0][1])