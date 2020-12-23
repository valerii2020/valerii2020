a = int(input("Enter a number "))
b = int(input("Enter another number "))

sum = 0

while a < b:
    a += 1
    if a > 0:
        sum += a
else:
    result = f'Your result is {sum}'
    print(result)