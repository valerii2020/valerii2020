a = input("введите а: ")
a = int(a)

b = input("введите b: ")
b = int(b)

c = input("введите c: ")
c = int(c)

D = b**2 - 4*a*c
print("x1 =", (-b + D**0.5) / (2*a))
print("x2 =", (-b - D**0.5) / (2*a))

# if D > 0:
#     print("x1 =", (-b + D**0.5) / (2*a))
#     print("x2 =", (-b - D**0.5) / (2*a))
# elif D == 0:
#     print("x =", -b / (2*a))
# else:  # D < 0
#     print("x1 =", (-b + D**0.5) / (2*a))
#     print("x2 =", (-b - D**0.5) / (2*a))
