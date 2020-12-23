a=input("введите число a")
a=int(a)
b=input("введите число b")
b=int(b)
c=input("введите число с")
c=int(c)
d=b**2-4*a*c
if d<0:
    print ("действительные корни отсутствуют")

elif d==0:
    print (-b/2*a)
else:
    sqrt=d**0.5
    x1=(-b+sqrt)/2*a
    x2=(-b-sqrt)/2*a
    print(x1)
    print(x2)


