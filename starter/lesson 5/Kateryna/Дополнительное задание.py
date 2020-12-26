def main():
    a = int(input('Enter the first number'))
    b = int(input('Enter the second number'))
    c = int(input('Enter the third number'))
    def calc(a, b, c):
        mean = int((a+b+c) / 3)
        return mean

    print(calc(a, b, c))

main()