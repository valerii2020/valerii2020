import math
x = int(input("Your value for x?"))

if -math.pi <= x <= math.pi:
    print(math.cos(3*x))
elif x < -math.pi or x > math.pi:
    print(x)

#or alternative

print(math.cos(3*x)) if -math.pi <= x <= math.pi else print(x)