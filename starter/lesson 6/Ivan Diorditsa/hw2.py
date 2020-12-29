def skip_spaces(s):
    only_letters = ''
    for c in s:
        if c == ' ':
            continue
        else:
            only_letters += c

    return only_letters


# s.lower()
def to_lower(s):
    only_lower = ''
    for c in s:
        if c == 'А':
            only_lower += 'а'
        else:
            only_lower += c

    return only_lower


def is_palindrome(s):
    s = skip_spaces(s)
    s = to_lower(s)

    def compare(i):
        if i == len(s):
            return True

        if s[i] == s[-i-1]:
            return compare(i+1)
        else:
            return False

    return compare(0)


print(is_palindrome('шалаш')) # T
print(is_palindrome('шалеш')) # F

print(is_palindrome('А роза упала на лапу азора')) # T
print(is_palindrome('А роза упала на лапу азара')) # F
