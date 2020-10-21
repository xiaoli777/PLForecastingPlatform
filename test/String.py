#String
print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"yes,\" he said.")
print('"Isn\'t," she said.')

s = 'First line.\nSecond line.'
print(s)

print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
    -h
    -H hostname
""")

print(3 * 'un' + 'ium')
print('Py''thon')
print("Py"'thon') # Only in text,not in expression
prefix = 'py'
print(prefix + 'thon')

text = ('Put '
        "off")
print(text)

word = 'Python' # Every value is unchangable.Can't change by giving single value.
print(word[0] + word[3] + word[-6])
print(word[0:2] , word[2:5])
print(word[:2] + word[2:])
print(word[0:-2])
print(word[4:42])

word = 'World'
print('J' + word[1:])
word = word + word
print(len(word))





