import re
'''
Write a short program that can check whether a password contains a digit.
'''

def contains_digit(string):
    result = re.search("[0-9]", string)
    if result:
        return True
    return False

print(contains_digit("KoolPa55w0rd"))
print(contains_digit("no digit :()"))
print(contains_digit("oneNnumber0"))