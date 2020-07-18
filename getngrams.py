
import nltk,re
from nltk.tokenize import sent_tokenize
from nltk import load


def processSentence(sentence,posLex,negLex,tagger):

    fourGrams=[]
    terms = nltk.word_tokenize(sentence)   #tokenize the sentence
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    if len(tagged_terms)>=4:    
        for i in range(len(tagged_terms)-3):# for every tagged term
            term1=tagged_terms[i] 
            term2=tagged_terms[i+1]
            term3=tagged_terms[i+2]
            term4=tagged_terms[i+3]
            if term1[0].lower()=='not' and ( term3[0].lower() in posLex or term3[0].lower() in negLex ) and re.match('NN',term4[1]): 
                fourGrams.append((term1[0],term2[0],term3[0],term4[0]))
        return fourGrams 
    return fourGrams        

def loadLexicon(fname):
   

    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex




if __name__=='__main__':
    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    print (processSentence("He is not a good leader so not a nice idea that he is leading team",loadLexicon("positive-words.txt"),loadLexicon("negative-words.txt"),tagger))



