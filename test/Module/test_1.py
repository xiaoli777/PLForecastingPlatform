import sys

import Test.T1
from Test.T1 import *

import test.Module.fibo

func()
func2()
print(Test.__path__)  # only package attribution

test.Module.fibo.fib(1000)
print(test.Module.fibo.fib2(100))
print(test.Module.fibo.__name__)

fib = test.Module.fibo.fib
fib(500)

print(dir(test.Module.fibo))
print(dir(fib))
print(dir(sys))

