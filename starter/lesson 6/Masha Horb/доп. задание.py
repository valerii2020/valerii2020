
def sum(current,max):
    if current<max:
        return current+sum(current+1,max)
    else:
        return max



x=input("введите конечное число x")
x=int(x)
a=input("введите начальное число a")
a=int(a)
print(sum(a,x))