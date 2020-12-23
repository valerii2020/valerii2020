import math

p=3.14
x=input("введите число x")
x=int(x)

if -p<=x<=p:
    y=math.cos(x*3)
elif x<-p or x>p:
    y=x
print(y)
