import re
'''
1. Give a regular expression that can be used to recognize a US phone number.
    Consider as many different ways a valid phone number is written in. 
    Write a short program that can identify US phone numbers from a given string of text.
'''

    # **  ( |^)(\+1[\- ]?|1[\- ]?)?\(?[0-9]{3}\)?[\- ]?[0-9]{3}[\- ]?[0-9]{4}(\D|$)
    # phones can have the international code +1 or just 1. So we need to check for that, then use the spacinging rule
    # ( |^)(\+1[\- ]?|1[\- ]?)? Breakdown:
        # ( |^)( ... )? <-- maintains that the stuff inside the parenthesis must be its own word or at the front,
            #  and looks for zero or one occurrance of the pattern described inside
        #  \+1[\- ]? <-- looks for the pattern "+1" followed by one or zero occurrances of a space or a dash
        # | <-- says that it will accept either the above pattern or the below one
        # 1[\- ]? <-- looks for the pattern "1" followed by one or zero occurrances of a space or dash

    # \(? <-- is a parenthesis character, the question mark afterwards says theres either one or none
    # [0-9]{3} <-- is 3 digits 0-9
    # \)? <-- same as the open parenthsis
    #     The above set accounts for the first three digits of a phone number, either encased in parenthesis or not

    # [\- ]? <-- This is asking for a dash (shown by the \-) or a space occurring either one or zero times
    #     The above accounts for the transition from the are code to the next three numbers
    
    # [0-9]{3} <-- same as above
    # [\- ]? <-- same as above
    #     The above accounts for the next three numbers, and the transition to the last four numbers

    # [0-9]{4} <-- this is the final four digits of the number
    
    # (\D|$) <-- maintains that what comes next can NOT be a digit (the phone number would be too long) 
    #   or may be the end of the sentence entirely. This allows for all types of punctuation which could 
    #   follow after a number in a sentence. (There's probably better ways to do this)

    


def is_phone_number(string):
    result = re.search(r"( |^)(\+1[\- ]?|1[\- ]?)?\(?[0-9]{3}\)?[\- ]?[0-9]{3}[\- ]?[0-9]{4}(\D|$)", string)
    if result:
        return True
    return False

def run_positive_tests():
    phone_numbers = ["(469)-3251245", "(469) 325-1245", "(469) 325 1245", "469-3251245", "469-325-1245", "4693251245", "469-3251245", "(469)-3251245", "469-325-1245", "1(469)-3051245", "+1(469) 325-1245", "1 (469) 325 1245", "+1 469-3251245", "1-469-325-1245", "+1-4693251245"]

    for number in phone_numbers:
        print(f"Number is: {number} it should pass")
        if not is_phone_number(number):
            print(f"---\nSomething went wrong. {number} should've passed, but it did NOT't.\n---")

    print("All positive tests finished!\n")

def run_negative_tests():
    bad_phone_numbers = ["(0469)-3251245", "(49) 325-1245", "(469) 325 12450", "469--3251245", "46932512450980897980", "469-325124-5", "(469)-325(1245", "469(325)1245", "9(469)-3051245", "+(469) 325-1245", "-469-325-1245", "(+1-4693251245)"]

    for number in bad_phone_numbers:
        print(f"Number is: {number} it should not pass")
        if is_phone_number(number):
            print(f"---\nSomething went wrong. {number} should NOT have passed, but it slipped through.\n---")

    print("All negative tests finished!")

run_positive_tests();
run_negative_tests();
print(f"\nTesting full sentences...")
good_sentences = ["My phone number is 123 432 8900.", "Here's my number: 1 (232) 191-0909", "8281024321's the way to go for me!"]
bad_sentences = ["Oh sure, my number is totally +9 (909) 9.", "Did you know there's probably over 100000 phone numbers?", "For real this time--432-143-1222"]

for sentence in good_sentences:
    print(f"The following sentence should pass: '{sentence}'")
    if not is_phone_number(sentence):
        print("---\nSomething went wrong. The above sentence should've passed, but it did NOT't.\n---")

print("\nOnto sentences with bad numbers...")

for sentence in bad_sentences:
    print(f"The following sentence should pass: '{sentence}'")
    if is_phone_number(sentence):
        print("---\nSomething went wrong. The above sentence NOT have passed, but it slipped through.\n---")