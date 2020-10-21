#ValueError
while True:
    try:
        x = int(input("number:"))
        print(x)
        break
    except ValueError as VE:
        print("ERROR: {0},\n"
              "ERRORType: {1},\n"
              "ERRORArgs:{2},\n"
              "Try again".format(VE,type(VE),VE.args))

#raise NameError('HiThere1')

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('Value:',e.value)
#
# raise MyError("Opps!")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:  #forever
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide('2', '1')

