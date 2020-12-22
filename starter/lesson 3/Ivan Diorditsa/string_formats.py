x = 5
y = 2

s = 'результат деления ' + str(5 / 2)
print(s)

# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
s1 = 'результат деления %.20f %d' % (5 / 2, -1)
print(s1)
s2 = 'числа %d %d "%s" %%' % (10, 20, 'мама')
print(s2)

# https://docs.python.org/3/library/string.html#formatstrings
s3 = 'результат деления {1} {0}'
s3 = s3.format(5 / 2, 10)
print(s3)

# TEMPLATE = 'добро пожаловать {}'
# name = input('введите имя')
# print(TEMPLATE.format(name))

# f-strings
name = 'Ivan'
s4 = f'добро пожаловать {name} {id(name)=}'
print(s4)

print('добро пожаловать', 'Иван')
