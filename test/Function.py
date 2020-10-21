#Function
def fib(n):#return None
    """Print a Fibonacci series up to n.""" #optional
    a, b = 0, 1
    while a < n:
        print(a , end = ' ')
        a, b = b, a+b
    n = 1000
    print(n)

print(fib.__doc__)

n = 2000
print(n)
fib(n)
f = fib
f(n)
print(n)
print(f(n))

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.insert(0,a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

def ask_ok(prompt, retries = 4, complaint = 'Yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('Uncooperative user')
        print(complaint)

# ask_ok('Do you really want to quit?')
# ask_ok('Do you really want to quit?',2)
# ask_ok('Do you really want to quit?', 2, 'Come on, only yes or no!')

i = 5
def f(arg = i):#Default only evaluate one time
    print(arg)

i=6
print(f())
print(f(i))

def f(a, L = []):#changable obj, accumulate
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L = None):#None accumulate
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def cheeseshop(kind, *arguments, **keywords):#*argument receive FP,**keywords receive FO which has keyword
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)#The number of '-' are 40
    keys = sorted(keywords.keys())#sort
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger","It's very runny,sir.",
           "It's really very, VERY runny,sir.",
           shopkeeper = "Micheal Palin",
           clinet = "John Cleese",
           sketch = "Cheese Shop Sketch")

def write_multiple_items(file, separator, *args):#changable args
    file.write(separator.join(args))

def concat(*args, sep = '/'):
    return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep = "."))

print(list(range(3, 6)))
print([3, 6])
args = [3, 6]
print(list(range(*args)))#use * to seperate args

def parrot(voltage, state = 'a stiff', action = 'voom'):
    print("-- This parrot wouldn't ", action, end = " ")
    print("if you put", voltage, "volts through it.", end = ' ')
    print("E's", state, "!")

d = {"voltage": "four million","state":"bleedin' demised","action": "VOOM"}
parrot(**d)

def make_incrementor(n):
    return lambda x : x + n
f = make_incrementor(42)
print(f(0))
print(f(3))

l = map(lambda x : x ** 2,[y for y in range(10)]) #anonymous

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key = lambda pair : pair[1])
print(pairs)

def add_end(L = [ ]):
    L.append('end')
    return L
print(add_end([1, 2, 3]))
print(add_end(['a', 'b', 'c']))
print(add_end())
print(add_end())
print(add_end([1, 2, 3]))
print(add_end(['a', 'b', 'c']))
print(add_end())
print(add_end())

l = (1, 2, 3, 4)#unchangable
print(len(l))
m = [1, 2, 3, 4]#changable
print(len(m))

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city = "Beijing", job = 'Student')

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)

def f(ham : 42, eggs : int = "spam") -> "Nothing":
    print("Annotations :", f.__annotations__)
    print("Agruments :", ham, eggs)
f("BIGHAM")
l = f("BIGHAM")
print(l) # return None

11111111111111111111111111111111111111111111111111111111111111111111111111111111

print("Check")
