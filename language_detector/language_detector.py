#!/usr/bin/env python
# Run command python language_detector.py data/train/en/all_en.txt data/train/es/all_es.txt data/test/ from language_detector directory

from optparse import OptionParser
import os, logging, re
import collections
import numpy as np


def preprocess(line):
    ## get rid of the staff at the end of the line
    line = line.rstrip()
    ## lower case
    line = line.lower()
    ## remove everything except characters and white space
    line = re.sub("[^a-z ]", '', line)

    tokens = line.split()
    ## update this when working with trigrams
    ## you can also change the preprocessing (keep numbers, do not lower case, etc.)
    tokens = ['$'+token+'$' for token in tokens]
    
    return tokens



def create_model(path):
    ## This is just some Python magic ...
    ## unigrams will return 0 if the key doesn't exist
    unigrams = collections.defaultdict(int)
    ## and then you have to figure out what bigrams will return
    bigrams = collections.defaultdict(lambda: collections.defaultdict(int))

    f = open(path, 'r',  encoding="utf8")
    ## You shouldn't visit a token more than once
    for l in f.readlines():
        tokens = preprocess(l)
        
        if len(tokens) == 0:
            continue
        for token in tokens:
            ########################################
            ## YOUR CODE GOES HERE
            ## Update the counts for unigrams and bigrams
            ########################################   
            # We're given the tokens but we need to make bigrams out of the CHARACTERS
            prev_unigram = None
            for letter in token:
                # Add the letter to the unigrams
                unigrams[letter] = unigrams.get(letter, 0) + 1
                # Construct the bigram (if we have enough letters)
                bigram = ''
                if prev_unigram:
                    bigram = f"{prev_unigram}{letter}"
                    # Add the two letters to the bigrams
                    bigrams[prev_unigram][letter] += 1

                # Save the current letter as prev letter for next iteration
                prev_unigram = letter


    ####################################################     
            
            
    vocab_size =  len(unigrams) # or 26
    # print("unigrams: {}".format(unigrams))
    # print("bigrams: {}".format(bigrams))
    ## After calculating the counts, calculate the smoothed log probabilities
    # here, prob['a']['b'] means probability of 'a' given 'b', prob['a']['b'] = count('ba')/count('b')
    prob = collections.defaultdict(lambda: collections.defaultdict(int))     
    # all_chars = "".join([k for k in unigrams.keys()]) #or all_chars = 'abcdefghizklmnopqrstuvwxyz$'
    all_chars = list(unigrams.keys()) # Modification provided by Given
    # print("all_chars: {}".format(all_chars))
    
    
    
    for c1 in all_chars:
        for c2 in all_chars:
            prob[c1][c2] = (np.log( (bigrams[c2][c1]+1)/(unigrams[c2] + vocab_size) ))
    
    # print("prob: {}".format(prob))
    ## return the actual model   

  
    '''
    for c in ['a', 'w']:
        print ("============================================================")
        print ("Count of %4s in %s: %6s\t(from unigrams dictionary, before calculating the smoothed log probabilities)" % ("'"+c+"'", path, unigrams[c]))
        counts = 0
        for c2 in bigrams[c]:
            print ("Count of %s%s in %s: %6s\t(from bigrams  dictionary, before calculating the smoothed log probabilities)" % ("'"+c, c2+"'", path, bigrams[c][c2]))
            counts += bigrams[c][c2]
        print ("============================================================")
        # This assert statment will abort the execution unless the count of c equals the sum of the counts of all bigrams that start with c
        # When you are developing, adding this kind of asserts may help you catching bugs early.
        # print("bigrams: {}".format(bigrams))
        assert unigrams[c] == counts
    '''    
    
   
    return prob

def predict(file, model_en, model_es):
    
    # if language == "en": model = model_en
    # else: model = model_es
    
    prediction = None
    prob_en = 0.0
    prob_es = 0.0
    
    f = open(file, 'r',  encoding="utf8")
    ## You shouldn't visit a token more than once
    ########################################
    ## YOUR CODE GOES HERE    
    ## - remember to do exactly the same preprocessing you did when creating the model
    ## - you may want to use an additional method to calculate the probablity of a text given a model
    for l in f.readlines():
        tokens = preprocess(l)
        
        if len(tokens) == 0:
            continue
        for token in tokens:
            prev_unigram = None # For getting the previous letter
            for letter in token:
                if prev_unigram:    # Once we can construct the x given y, find its probabilty in the EN and ES models                
                    prob_en += model_en[letter][prev_unigram]
                    prob_es += model_es[letter][prev_unigram]

                # Save the current letter as prev letter for next iteration
                prev_unigram = letter

    ######################################## 
    prediction = "English" if prob_en > prob_es else "Spanish"
    prediction = "None" if prob_en == prob_es else prediction
    return prediction


def main(en_tr, es_tr, folder_te):
    ## DO NOT CHANGE THIS METHOD

    ## STEP 1: create a model for English with en_tr
    model_en = create_model(en_tr)
    # print(f"\n\nENGLISH MODEL: {model_en}\n\n")

    ## STEP 2: create a model for Spanish with es_tr
    model_es = create_model(es_tr)

    ## STEP 3: loop through all the files in folder_te and print prediction
    folder = os.path.join(folder_te, "en")
    print ("Prediction for English documents in test:")
    for f in os.listdir(folder):
        f_path =  os.path.join(folder, f)
        print ("%s\t%s" % (f, predict(f_path, model_en, model_es)))        
        
    
    folder = os.path.join(folder_te, "es")
    print ("\nPrediction for Spanish documents in test:")
    for f in os.listdir(folder):
        f_path =  os.path.join(folder, f)
        print ("%s\t%s" % (f, predict(f_path, model_en, model_es)))

        


if __name__ == "__main__":
    ## DO NOT CHANGE THIS CODE

    usage = "usage: %prog [options] EN_TR ES_TR FOLDER_TE"
    parser = OptionParser(usage=usage)

    parser.add_option("-d", "--debug", action="store_true",
                      help="turn on debug mode")

    (options, args) = parser.parse_args()
    if len(args) != 3:
        parser.error("Please provide required arguments")

    if options.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    main(args[0], args[1], args[2])
