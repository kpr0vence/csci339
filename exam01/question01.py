import re

'''
find sequences of lowercase letters joined with an underscore. for example: 
"aab_cbbbc" would be a match where as "aab_Abbbc" would not be a match 
'''
def task_a(text: str) -> str:
    result = re.search(r'[a-z]+_[a-z]+', text)
    if result:
        return f"There is a match: '{result.group()}'"
    return "There is no match"

'''
match a string that contains only upper and lowercase letters, numbers, 
and underscores. for example: "Python_Exercises_1" would be a match
where as "Hello everyone!" would not be a match 
'''
def task_b(text: str) -> str:
    result = re.search(r'^([a-zA-Z_\d]+)$', text)
    if result:
        return f"There string is valid: '{result.group()}'"
    return "There string is not valid."

'''
match a us social security number in the format XXX-XX-XXXX where X 
represents a digit 
'''
def task_c(text:str) -> str:
    result = re.search(r'(\s|^)\d{3}-\d{2}-\d{4}(\s|$)', text)
    if result:
        return f"There is a match: '{result.group()}'"
    return "There is no match"

'''
match a C variable declaration of primitive types like int, char and float 
for example: "int myVariable;" will be a match but "float 1stFloat:" will
not be a match 
    Names can contain letters, digits and underscores --> "\W"
    Names must begin with a letter or an underscore (_) --> "^([a-zA-z]|_)"
    Reserved words (such as int) cannot be used as names
'''
def task_d(text:str) -> str:
    text_split = text.split(" ")
    var_name = text_split[1]    # get the variable name separate from the type
   
    # 0. Check for spaces
    if (len(text_split) > 2):
        return "You can not have spaces in your variable, invalid name"
    # 1. Check for the semicolon at the back
    if (var_name[-1] != ";"):
        return "There is no semicolon at the end, invalid name"

    var_name = var_name[0:-1]   # get rid of the semicolon for further analysis

    # 2. Check for reserved words
    if (re.search(r'^(int|float|char)$', var_name)):
        return "You can not name a variable a reserved word, invalid name"

    # 3. Check if it has non-word characters terminate early
    if (re.search(r'\W', var_name)):
        return "Special characters are not allowed, invalid name"

    # 4. Check it begins with letter or underscore
    if (re.search(r'^([a-zA-z]|_)', var_name)) is None:
        return "The name must begin with a letter or underscore, invalid name"

    # If it passes all of these, it's good
    return f"{var_name} is a valid name"

'''
match a US 7 digit or 11 digit zip-code for example:
"TX-76201" or "TX 76201" or "TX 76201-1234" will all be matches 
'''
def task_e(text: str) -> str: 
    '''
    2 letters (uppercase)
    followed by a space or dash
    followed by 5 digits
    OPTIONALLY followed by a dash and 4 digits
    '''
    result = re.search(r'(\s|^)[A-Z]{2}( |-)\d{5}(-\d{4})?(\s|$)', text)
    if result:
        return f"There is a match: {result.group()}"
    return "There is no valid match"


def main():
    print(task_a("aab_cbbc"))
    print(task_a("aab_Abbbc"))
    print(task_a("WoorfsdadsSSaab_cbbc"))

    print(task_b("Python_Exercises_1"))
    print(task_b("Hello everyone!"))

    print(task_c("483-42-5323"))
    print(task_c("4838-42-5323"))
    print(task_c("4838-425323"))

    print(task_d("int myVariable;"))
    print(task_d("float 1st Float;"))
    print(task_d("float 1stFloat;"))

    print(task_e("TX-76201"))
    print(task_e("TX 76201"))
    print(task_e("TX 76201-1234"))
    print(task_e("TX 76201-2"))



if __name__=="__main__":
    main()
