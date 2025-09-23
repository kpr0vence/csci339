import re
# 2. Split the following sentences into an array that contains only its words.
#   "Tom cried: 'What is going on?'. Then he left the room."
def clean_word(word):
    return re.sub(r"[^a-zA-Z0-9\s]", "", word)  

def split_and_clean(sentence):
    # Step 1: split the string into tokens using their white space
    tokens = sentence.split(" ")

    # Step 2: clean them by replacing all non letters with empty space
    for i in range(len(tokens)):
        if not tokens[i].isalnum():
            # We've found a place we need to clean
            tokens[i] = clean_word(tokens[i])            

    return tokens

print(split_and_clean("Tom cried: 'What is going on?'. Then he left the room."))