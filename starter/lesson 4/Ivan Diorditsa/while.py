op = input("введите операцию (tan или +): ")
print(f'{op=}')

while op != 'tan' and op != '+':
    print('неправильная операция, попробуйте ещё раз')
    op = input("введите операцию ")
else:
    print("введена правильная операция", op)

print("вышли из цикла")
