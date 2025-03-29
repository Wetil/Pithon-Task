import re

def is_palindrome(string):
    string = (re.sub(r'[^\w\s]', '', str(string)).lower()).replace(" ", "")
    str2 = string[::-1]

    if (string == str2):
        print("True")
    else:
        print("False")

is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra")
