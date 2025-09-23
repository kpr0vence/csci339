import re
'''
2. Give a regular expression that can recognize an email address. Write a short Python 
   program that can identify email addresses from a given string of text.
'''

# Email addresses can varry a LOT. I'm going to simplify to the most common rules to implement 
# into my regEx (reference: https://en.wikipedia.org/wiki/Email_address#Local-part)
    # The rule about periods in the local-part is that they can't be on the beginning or the end

# Breaking down the regEx string I've made
# ** [\w\d\+][\w\d\+\.]*[\w\d\+]@[\w\d]+\.[\w\d]+
'''
[\w\d\+] <-- looking for any ONE letter,  number, or plus (this had to be seperate from the next statement, because it allows periods)
[\w\d\+\.]* <-- after the first character, there can be any number of alphanumeric or plus or period symbols
[\w\d\+] <-- same as the first one, disallows periods from being at the end of the local part of the email address
@ <-- there MUST be an at symbol
[\w\d]+ <-- there must be at least one alphanumeric character in the first part of the address
. <-- there MUST be a period denoting the two parts of the address behind the at symbol
[\w\d]+ <-- same as above
'''

def is_email(string):
    regEx_chunk = r"[\w\d\+][\w\d\+\.]*[\w\d\+]@[\w\d]+\.[\w\d]+"
    result = re.search(regEx_chunk, string)
    if result:
        print(f"Your email was found in the string: {string[result.start() : result.end()]}")
        return True
    return False


print(is_email("0.lvjnsk+.email@skjv.sdv"))
print(is_email("My email is definitely 123myName@xyc")) # missing the last part shouldn't return true
print(is_email("My email is definitely 123myName@xyc.com")) 