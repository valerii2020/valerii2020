PIN_CODE = 1234
money = 100

pin = input("введите пин-код ")
pin = int(pin)
if pin == PIN_CODE:
    print("правильный пин")
else:
    print("неправильный пин")

amount = input("сколько денег вы хотите снять? ")
amount = int(amount)
if amount <= money:
    print("вот ваши", amount, "гривен")
    money = money - amount
    print("на вашем счету осталось", money, "гривен")
else:
    print("у вас недостаточно денег")
