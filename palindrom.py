#it is a string that reads the same forward and backward .
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("rainy")) 