
import os.path
from index_utils import FILTER, DOC_DOCLEN_FREQ_DIC, INVERTED_INDEX_DIC
import pickle



# we read the tsv files from the folder TSV 
input_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'


## there are dictionary of dictionary because is easy to read
'''
{ word_id : {doc_id : tfidf,
             doc_id : tfidf,
             doc_id : tfidf }, 
  word _id: {doc_id : tfidf,
             doc_id : tfidf,
             doc_id : tfidf,
             doc_id : tfidf}
  }
'''

# is a dictionry with as key the word and as value another dictionary with key the number of the document and as value the frequency of the word in this document
direct_index = {}

#the inverted index with as key the words
Inverted_index_words = {}

#the inverted index with as key the words_number read from the Vocabulary
Inverted_index = {}

# as key the word as value the number
Vocabulary = {}

# as key the number of the document as value his length after cleaning
Length_Doc = {}

# 30000 - number of empty docs
Number_of_documents = 29982

N = 30000
i = 0
while i < N:
    print(i)
    # read the i-th tsv
    completeName_input = os.path.join(input_path, 'article_' + str(i) + '.tsv')
    with open(completeName_input, 'r') as input_file:
        intro_plot = input_file.readline()
    # select only the intro and the plot
    intro_plot = intro_plot.split('\t')[1:3]
    # make a string
    intro_plot = str(intro_plot[0]) + ' ' + str(intro_plot[1])
    # filter this string
    Document = FILTER(intro_plot)
    # save the length of the document
    Length_Doc[i] = len(Document) 
    
    # make the direct index
    DOC_DOCLEN_FREQ_DIC(Document, direct_index, i)
    
    
    
    i += 1

# save the inverted index with the words as key
INVERTED_INDEX_DIC(direct_index, Inverted_index_words, Length_Doc, Number_of_documents)

# create the Vocabulary and the real inverted index
counter = 0
for i,j in Inverted_index_words.items():
    Vocabulary[i] = counter
    Inverted_index[counter] = j
    counter += 1


c = []

for i in  Inverted_index_words:
    c.append(i)
    
file = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'

# save the 3 dictionaries as pkl
with open(file+'Inverted_index.pkl', 'wb') as fp:
    pickle.dump(Inverted_index, fp, protocol = pickle.HIGHEST_PROTOCOL)
    
with open(file+'Vocabulary.pkl', 'wb') as fp:
    pickle.dump(Vocabulary, fp, protocol = pickle.HIGHEST_PROTOCOL)

with open(file+'Length_doc.pkl', 'wb') as fp:
    pickle.dump(Length_Doc, fp, protocol = pickle.HIGHEST_PROTOCOL)
