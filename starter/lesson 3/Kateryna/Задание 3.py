import math

a = int(input("Please enter the first number "))
b = int(input("Please enter the second number "))
c = int(input("Please enter the third number "))
root = b**2 - 4*a*c
if root >= 0:
    number2 = root ** 0.5

    m1 = (-b + number2)
    m2 = (-b - number2)

    x1 = m1 / (2 * a)
    x2 = m2 / (2 * a)

    equation1 = a * (x1 ** 2) + b * x1 + c
    equation2 = a * (x2 ** 2) + b * x2 + c

    result1 = equation1 == 0
    result2 = equation2 == 0

    print( result1 , " ", result2)

else:
    result = -(b / (2*a))
    print(result)
