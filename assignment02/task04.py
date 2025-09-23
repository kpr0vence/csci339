import re
'''
Define a rule for passwords, read a password from the user using prompt, and check it.

'''
# ** (?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])
#  Each of the sections (enclosed in parenthesis) is called a positive look ahead. It is what
#  lets the three requirements come in any order (help from here: 
# https://stackoverflow.com/questions/4389644/regex-to-match-string-containing-two-names-in-any-order and
#  here: https://www.regular-expressions.info/lookaround.html)
# (?=.*[a-z]) <-- Is apositive lookahead the is asking for any lowercase letter. The .* before the [a-z]
# Makes it so that it can appear anywhere in the string (by having any number of any characters in front of it)
# (?=.*[A-Z]) <-- Same thing but for any capital letter
# (?=.*[0-9]) <-- Same thing but for any digit


def valid_password(password):
    sequence = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])"
    result = re.search(sequence, password)
    if result:
        return True
    return False

while True:
    password = input("Please make your password, it must contain at least one capital letter, lower case letter, and digit: ")
    if valid_password(password):
        print("\nPassword Accepted!")
        break
    print("That password does not contain the specified phrase, please try another password.")

    # Razzy is the name of a stuffed animal that I have that I like very much!