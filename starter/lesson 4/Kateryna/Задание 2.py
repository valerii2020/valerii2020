x = int(input("Enter a number "))

factorial = 1

for a in range(1,x+1):
    factorial = factorial * a

result = f'Your result is {factorial}'
print(result)
