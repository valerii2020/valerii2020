import math

operation = input(""" Pick an operation:
1. +
2. -
3. *
4. /
5. ^
6. sin
7. cos 
8. tan
""")
result = "Your result is {0}"

if operation == "+" or operation == "1":
    first = int(input("Your first number "))
    second = int(input("Your second number "))
    sum = first + second
    print(result.format(sum))
elif operation == "-" or operation == "2":
    first = int(input("Your first number "))
    second = int(input("Your second number "))
    subtr = first - second
    print(result.format(subtr))
elif operation == "*" or operation == "3":
    first = int(input("Your first number "))
    second = int(input("Your second number "))
    multi = first * second
    print(result.format(multi))
elif operation == "/" or operation == "4":
    first = int(input("Your first number "))
    second = int(input("Your second number "))
    divis = first / second
    print(result.format(divis))
elif operation == "^" or operation == "5":
    first = int(input("Your first number "))
    second = int(input("Your second number "))
    h = first ** second
    print(result.format(h))
elif operation == "sin" or operation == "6":
    first = int(input("Your number "))
    s = math.sin(first)
    print(result.format(s))
elif operation == "cos" or operation == "7":
    first = int(input("Your number "))
    c = math.cos(first)
    print(result.format(c))
elif operation == "tan" or operation == "8":
    first = int(input("Your number "))
    t = math.cos(first)
    print(result.format(t))
else:
    print("a problem was detected")