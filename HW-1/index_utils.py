from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import numpy as np

# generate the stop-words
stopWords = set(stopwords.words('english'))

# this function work for a generic string, such as a document or the query
def FILTER(string):
    # we are going to filter the string
    string = string.lower()
    string = string.replace("'", "")
    # tokenize the string
    tokenizer = RegexpTokenizer("[\w']+")
    Vector = tokenizer.tokenize(string)
    # removing the stop-words
    wordsFiltered = []
    for w in Vector:
        if w not in stopWords:
            wordsFiltered.append(w)
    #stemmer
    porter = PorterStemmer()
    ListOfWords = [porter.stem(word) for word in wordsFiltered]
    return ListOfWords

# we use this function to create the direct index
# is a dictionry with as key the word and as value another dictionary with key the number of the document and as value the frequency of the word in this document
def DOC_DOCLEN_FREQ_DIC(Document, direct_index, i):
    Document = Counter(Document)
    for word, frequence in Document.items():
        if word not in direct_index:
            direct_index[word] = {i: frequence}
        else:
            direct_index[word][i] = frequence
    return 

# we use this function to create the inverted index 
def INVERTED_INDEX_DIC(direct_index, Inverted_index, Length_Doc, Number_of_documents):
    for key, Doc_Freq in direct_index.items():
        Inverted_index[key] = {}
        for doc, freq in Doc_Freq.items():
            if key not in Inverted_index:
                Inverted_index[key] = {doc: (freq/ Length_Doc[doc])*np.log10(Number_of_documents/len(Doc_Freq))}
            else:
                Inverted_index[key][doc] = (freq/ Length_Doc[doc])*np.log10(Number_of_documents/len(Doc_Freq))
    
    return 


