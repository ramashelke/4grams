# 4grams

The script defines the following function:

processSentence(sentence,posLex,negLex,tagger): The parameters of this function are a sentence (a string), a set of positive words, a set of negative words, and a POS tagger.  The function returns a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>

For example: not a good idea
