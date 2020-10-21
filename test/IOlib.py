from string import Template

from builtins import print

t = Template('${village}flok send $$10 ti $cause.')
t1 = t.substitute(village = 'Bittubggam', cause = 'the ditch fund')
print(t1)

from decimal import *
print(Decimal('1.0000') % Decimal('0.1000'))

print(1/10 + 2/100 + 5/1000)
print(round((0/2 + 0/4 + 1/8), 8))
print(0.333)
print(eval(repr(0.1)))

print(0.1 + 0.1 + 0.1 == 0.3)   # percision, so many outcome you cann't imagine
print(str(0.1))

#import fractions
from fractions import *
print(Fraction(1, 10) + Fraction(1, 3))
print(Fraction(1, 10).__repr__())
print(repr(Fraction(1, 10)))
print(0.1.as_integer_ratio())
print(0.3.as_integer_ratio())
print((3602879701896397 / 36028797018963968) * 3 == (5404319552844595 / 18014398509481984))
print((3602879701896397 / 36028797018963968) +
      (3602879701896397 / 36028797018963968) +
      (3602879701896397 / 36028797018963968) == (5404319552844595 / 18014398509481984))
print((3602879701896397 / 36028797018963968) == 0.1)
print(format(Decimal.from_float(0.1)))



