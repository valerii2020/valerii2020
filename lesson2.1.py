pin_code = 1234
money = 100


pin =int(input("enter your pin "))
if pin == pin_code:
    print("Pin is correct")
else:
    print("Pin is incorrect")


amount = int(input("How much money would you like? "))
if amount <= money:
    print("Here is your", amount, "pounds")
    money = money-amount
    print("You have", money, "left on your account")
else:
    print("Insufficient amount on account, unable to complete the transaction ")