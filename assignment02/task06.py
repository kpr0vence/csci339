import re
'''
6. Input a one page long file and tokenize the text into words. Also get rid of "stop words". Use regular expressions.
'''

def split_and_clean(text):
    stop_words = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
  ]
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', "", text,)   # Get rid of punctuation
    tokens = re.split(r'\W', cleaned)   # Split them
    # I'm sure there are ways I could clean the stop words out with regex, but the only ones I could think of would be a looooong
    # regEx where I just type the words out
    new_words = []
    for token in tokens:
        if (token.lower() not in stop_words):   # If it's not a stop word add it to the new list of words
            new_words.append(token)
    
    return new_words

# Proof of concept using regex for the matching
def split_and_clean2(text):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', "", text,)   # Get rid of punctuation
    tokens = re.split(r'\W', cleaned)   # Split them
    new_words = []
    for token in tokens:
        if (re.match(fr"(the|and|because)", token, flags=re.IGNORECASE)):
            continue
        else:
            new_words.append(token)
    return new_words

'''Main Section'''
try:
    with open('lordOfTheFliesSelection.txt', 'r') as file:
        content = file.read()
        first = split_and_clean(content)
        # second = split_and_clean2(content)
        print(first)
        # print(second)
        
except Exception:
    print("Something went wrong...")
  
