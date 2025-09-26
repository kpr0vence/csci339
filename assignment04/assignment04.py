import spacy
# Load the installed model "en_core_web_md"
nlp = spacy.load("en_core_web_md")  # Has to be the md one, so that it can do similarity analysis.

# I used a venv to run SpaCy, in case that is important

def tokenize(doc) -> list[str]:
    tokens = [token.text for token in doc]
    print(tokens)
    return tokens

def pos_tag_fine_grained(doc) -> list[str]:
    pos_tokens = [token.tag_ for token in doc]
    print(f"Fine Grained: {pos_tokens}")
    return pos_tokens

def pos_tag_coarse_grained(doc) -> list[str]:
    pos_tokens = [token.pos_ for token in doc]
    print(f"Coarse Grained: {pos_tokens}")
    return pos_tokens

def named_entities(doc) -> list[str]:
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named Entities: {named_entities}")
    return named_entities

def lemmatize(doc) -> list[str]:
    lemmatized = [token.lemma_ for token in doc]
    print(f"Lemmas: {lemmatized}")
    return lemmatized

def compare_similarity(line1: str, line2: str):
    doc1 = nlp(line1)
    doc2 = nlp(line2)
    similarity = doc1.similarity(doc2)
    print(f"Similarity of '{line1}' and '{line2}'--> {similarity}")
    return similarity

def preprocess(text: str) -> list[str]:
    '''
        Lowercases the text, 
        Lemmatizes each token,
        Removes punctuation symbols,
        Removes stop words
    '''
    text = text.lower()
    doc = nlp(text)

    # Lemmatize and save each non-stop non-token word. 
    # syntax hint here: https://www.educative.io/answers/how-to-remove-stop-words-using-spacy-in-python
    cleaned = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    print(f"Preprocessed: {cleaned}")
    return cleaned


def main():
    lines: list[string] = ["Asheville is my most favorite place to live in.", 
        "There are 31 days in the month of January.", 
        "What are your plans for the summer?", 
        "I plan to go to Hawaii for a short trip."]

    for line in lines:
        print(f"------\n{line}:")
        doc = nlp(line)     # The doc object holds the tokens and info about them
        tokenize(doc)
        pos_tag_fine_grained(doc)
        pos_tag_coarse_grained(doc)
        named_entities(doc)
        lemmatize(doc)
        preprocess(line)
        print("------\n")

    compare_similarity(lines[0], lines[3])


if __name__ == "__main__":
    main()


