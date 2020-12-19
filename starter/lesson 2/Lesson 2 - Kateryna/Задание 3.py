import math

a = input("Please enter the first number ")
b = input("Please enter the second number ")
c = input("Please enter the third number ")

a= int(a)
b= int(b)
c= int(c)

number1 = b**2 - 4*a*c

control = number1 > 0

print("Control is " + str(control))

number2 = number1 ** 0.5
print(number2)

m1 = (-b + number2)
m2 = (-b - number2)


x1 = m1/(2*a)
x2 = m2/(2*a)

equation1 = a*(x1**2) + b*x1 + c
equation2 = a*(x2**2) + b*x2 + c
print(equation1, equation2)

result1 = equation1 == 0
result2 = equation2 == 0

print(result1, " ", result2)
