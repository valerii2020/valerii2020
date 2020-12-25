def name(p):
    print('Здравствуй ', p)

p = input('Введите имя ')
if not p:
    name('Валерий')
else:
    name(p)

