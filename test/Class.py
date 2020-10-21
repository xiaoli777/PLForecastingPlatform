#  Class Multisecceed override

def scope_test():
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        nonlocal spam   # close scope and reload
        spam = 'nonlocal spam'
    def do_global():   # global scope and reload
        global spam
        spam = 'global spam'
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return "hello world!"

x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
print(x.f())

class Dog:
    kind = 'canine'
    __fur = 'soft'   # private : forword 2 '_' at least, backword  '_' at best
    tricks = []   # sharing
    def __init__(self,name):
        self.name = name
        #self.tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)
    def alter_kind(self,kind):
        self.kind = kind
    def pf(self):
        print(self.__fur)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.alter_kind('Baby')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
print(d.tricks)
print(e.tricks)
print(d.__class__)
d.pf()

class BigDog(Dog):
    pass

g = BigDog('LALA')
print(g.kind)
print(g.name)
print(g.__class__)
print(isinstance(g, Dog))
print(issubclass(BigDog, Dog))
g.pf()
print(getattr(g, "name"))
setattr(g, "name", "XIXI")
print(g.name)

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except B:# Top-Down
        print("B")
    except C:
        print("C")
    except D:
        print("D")


class MyDog(Dog, MyClass):
    pass

# iterator
s = 'abc'
it = iter(s)
print(it)
print(id(it))
print(next(it))
print()

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    # def next(self):
    #     if self.index == 0:
    #         raise StopIteration
    #     self.index -= 1
    #     return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)
# print(rev.__next__())

print(MyClass.__dict__)

