#calculator program
import math

operator = (input("Пожалуйста, введите математический оператор "))

number1 = (int(input("Пожалуйста введите первое число ")))
number2 = (int(input("Пожалуйста введите второе число ")))

addition = "+"
division = "//"
minus = "-"
multiply = "*"
powered = "**"
cosinus = "cosinus"
tangens = "tan"


if operator == addition:
    print(number1 + number2)

elif operator == division:
    print(number1//number2)

elif operator == minus:
    print(number1-number2)

elif operator == multiply:
    print(number1*number2)

elif operator == powered:
    print(number1**number2)
elif operator == cosinus:
    math.cos(number1)
elif operator == tangens:
    math.tan(number1)
else:
    print("Please restart the program ")


# cannot do cosine and tangens





