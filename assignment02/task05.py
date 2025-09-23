import re
'''
use RegEx to split the following sentences into an array that contains only its words.
"Tom cried: 'What is going on?'. Then he left the room."
'''
sentence = "Tom cried: 'What is going on?'. Then he left the room."
cleaned = re.sub(r'[^a-zA-Z0-9 ]', "", sentence,)   # Use regex to cleanse all special characters from the sentence
split = re.split(r'\W', cleaned)    # then split the cleaned version
print(split)
