# 𝑎𝑥2+𝑏𝑥+𝑐=0

a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))


d = b**2-4*a*c

if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("This equation has one solutions: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print ("This equation has two solutions: ", x1, " and", x2)

