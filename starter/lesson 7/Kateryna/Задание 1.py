x = input("Enter some numbers: ")
x1 = x.split(", ")
x2 = []
for i in x1:
    x2.append(int(i))
print(x2)
print('The max number is ', max(x2))
print('The min number is ', min(x2))
print('The sum of your numbers is ', sum(x2))
print('The mean of your numbers is ', sum(x2) / len(x2))