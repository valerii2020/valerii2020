def check():
    str = input('Please enter a sentence ')
    palindrome = ''.join(reversed(str))
    if str == palindrome:
        print("It's a palindrome!")
        check()
    elif str == 'stop':
        print("Program is shutting down!")
    elif palindrome != str:
        print("It's not a palindrome!")
        check()


check()