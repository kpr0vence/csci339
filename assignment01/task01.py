# 1. Write a short program that can check whether a password contains a digit.

def contains_digit(password):
    for digit in range(1,10):
        if str(digit) in password:
            return True
    return False


print(f"Should not contain a digit --> {contains_digit("mypasswordisgood")}")
print(f"Should contain a digit --> {contains_digit("myp4ssw0rdisb4d")}")