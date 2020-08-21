#C:\Users\franc\Desktop\Data_science\Algorithmic_Methods_of_Data_Mining\ADM_hw3

import numpy as np
from index_utils import FILTER
import pickle
from functools import reduce
import pandas as pd
import os.path
import numpy as np
from collections import Counter


######################################## Search engine 1

def conjuntive_query(Query, Inverted_index, Vocabulary, Docs):
    for i in Query:
        # select all the docs with a specific word and appen this array to another array
        try:
            Docs.append(np.fromiter(Inverted_index[Vocabulary[i]].keys(), dtype=int))
        except: 
            pass
    # make the and
    if len(Docs) > 0:
        Films = reduce(np.intersect1d, Docs)
    else:
        Films = []
    return Films



def output_conjuntive_query(Films, input_path, Doc_Id_url):
    Title = []
    Intro = []
    Url = []
    # for each film selected we are going to save title, intro and url
    for i in Films:
        completeName_input = os.path.join(input_path, 'article_' + str(i) + '.tsv')
        with open(completeName_input, 'r', encoding="utf8") as input_file:
            document = input_file.readline()
        document= document.split('\t')
        Title.append(document[0])
        Intro.append(document[1])
        Url.append(Doc_Id_url[i])
        
    #create a dictionary
    Data = {'title' : Title,
            'intro' : Intro,
            'url' : Url
            }
   
    # make the dataframe 
    df = pd.DataFrame(data=Data)
    
    return df

######################################## Search engine 2
    

def output_second_score(Films, input_path, Score, Doc_Id_url, Film_Score):
    Title = []
    Intro = []
    Url = []
    Score_cosin = []
    # for each film selected we are going to save title, intro and url
    for i in range(len(Films)-1,-1,-1):
        completeName_input = os.path.join(input_path, 'article_' + str(Film_Score[Score[i]]) + '.tsv')
        with open(completeName_input, 'r', encoding="utf8") as input_file:
            document = input_file.readline()
        document= document.split('\t')
        Title.append(document[0])
        Intro.append(document[1])
        Url.append(Doc_Id_url[Film_Score[Score[i]]])
        Score_cosin.append(Score[i])
    #create a dictionary
    Data = {'title' : Title,
            'intro' : Intro,
            'url' : Url,
            'score' : Score_cosin
            }
   
    # make the dataframe 
    df = pd.DataFrame(data=Data)
    
    return df






######################################## Search engine 3

def search_composer_director(Films, input_path):
    # reading into the infobox the composer and the director
    Composers = []
    Directors = []
    if len(Films) != 0:
        for i in Films:
            completeName_input = os.path.join(input_path, 'article_' + str(i) + '.tsv')
            with open(completeName_input, 'r', encoding="utf8") as input_file:
                document = input_file.readline()
            document= document.split('\t')
            # filtering the words and adding to the array
            Composers.append(FILTER(document[8]))
            Directors.append(FILTER(document[4]))
    else:
        # if there are no movies with all the words in the query
        print('\n\n\nnothing for you')
    return Composers, Directors

def FREQ_value(Inverted_index, Vocabulary, Films):
    # we are interested in the frequency ie tf
    freq = []
    if len(Films) != 0:
        for i in Query:
            freq_word = []
            for j in Films:
                # select all the docs with a specific word and appen this array to another array
                try:
                    freq_word.append(Inverted_index[Vocabulary[i]][j]/np.log10(29982/len(Inverted_index[Vocabulary[i]])))
                except:
                    freq_word.append(0)
                    pass
            freq.append(freq_word)
    else:
        pass
    return freq
        
def COUNT_value():
    # we count the correspondences between directors and composers
    counter_film = []
    if len(Films) != 0:
        counter_film = []
        for k in range(len(Films)):
            counter_film.append(0)
            for i in Composers[k]:
                for j in composer:
                    if i == j:
                        counter_film[k] += 1
        
            for i in Directors[k]:
                for j in director:
                    if i == j:
                        counter_film[k] += 1
    else:
        pass
    return counter_film

def FINAL_SCORE():
    # we are going to sum all the frequence of the words into the docs and taking the mean
    if len(Films) != 0:
        Score_movie = [0 for i in range(len(Films))]
        for i in range(len(freq)):
            for j in range(len(Films)):
                Score_movie[j] += freq[i][j]
        # adding the special point if somthing match  
        for i in range(len(Score_movie)):
            Score_movie[i] = Score_movie[i]/len(Query)
            Score_movie[i] = Score_movie[i] + counter_film[i]*.25
    else:
        Score_movie = 0
    return Score_movie

def output_new_score(Films, input_path, Score_movie, Doc_Id_url, k, Film_score):
    Title = []
    Intro = []
    Url = []
    Score = []
    Score_movie = Score_movie[::-1]
    # for each film selected we are going to save title, intro and url
    for i in range(k+1):
        completeName_input = os.path.join(input_path, 'article_' + str(Film_score[Score_movie[i]]) + '.tsv')
        with open(completeName_input, 'r', encoding="utf8") as input_file:
            document = input_file.readline()
        document= document.split('\t')
        Title.append(document[0])
        Intro.append(document[1])
        Url.append(Doc_Id_url[Film_score[Score_movie[i]]])
        Score.append(Score_movie[i])
    #create a dictionary
    Data = {'title' : Title,
            'intro' : Intro,
            'url' : Url,
            'score' : Score
            }
   
    # make the dataframe 
    df = pd.DataFrame(data=Data)
    
    return df
    

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1	 # left = 2*i + 1 
    r = 2 * i + 2	 # right = 2*i + 2 
	# See if left child of root exists and is 
	# greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
	# See if right child of root exists and is 
	# greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
	# Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
        heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
	n = len(arr) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] # swap 
		heapify(arr, i, 0) 





######################################## Start the code


# folder with the tsv files
input_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'

# reading the dictionaries
file = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'
with open(file + 'Inverted_index.pkl', 'rb') as fp:
    Inverted_index = pickle.load(fp)

with open(file + 'Vocabulary.pkl', 'rb') as fp:
    Vocabulary = pickle.load(fp)

with open(file + 'Doc_Id_url.pkl', 'rb') as fp:
    Doc_Id_url = pickle.load(fp)

Length = {doc_id :[[],[]] for doc_id in range(30000) }
for word_id,doc_id_tfidf in Inverted_index.items():
    for doc_id, tfidf in doc_id_tfidf.items():
        Length[doc_id][0].append(word_id)
        Length[doc_id][1].append(tfidf)


# %%
# input for the user
while True:
    try:
        Choice = int(input('which search: 1, 2 or 3?  '))
        if Choice == 3:
            
            Query = input('amazing: the query is?  ')
            # maybe somthing as 'do you want specify the director?'
            k = input("HOW MANY DOCUMENTS YOU WANT?\nhe defolt value is 3, press enter if you don't have a preference  ")
            if k == '':
                k = 2
            else:
                k = int(k)-1
            composer = input("CHOOSE THE MUSIC COMPOSER. \nPress enter if you don't have a preference  ")
            director = input("CHOOSE THE DIRECTOR? \nPress enter if you don't have a preference  ")
            
            
            pass
        else:
            Query = input('amazing: the query is?  ')
        break
    except:
        print('try again')

# filtering the query
Query = FILTER(Query) 

# initialize two arrays
All_docs = []
Docs = []




# if conjuntive query
if Choice == 1:
    # search all the rigth movies
    Films = conjuntive_query(Query, Inverted_index, Vocabulary, Docs)
    if len(Films) == 0:
        print('Sorry but there is nothing for you, try again')
    else:
        #make the dataframe
        df = output_conjuntive_query(Films, input_path, Doc_Id_url)
        print(df)

if Choice == 2:
    
    # evaluating the tfidf for the query
    Query_counter = Counter(Query)
    Query_tfidf = {}
    for k,v in Query_counter.items():
        Query_tfidf[Vocabulary[k]] = (v/ len(Query))*np.log10((29982/len(Inverted_index[Vocabulary[k]]))+1)
    
    # use the conjuntive query
    Films = conjuntive_query(Query, Inverted_index, Vocabulary, Docs)
    if len(Films) == 0:
        print('Sorry but there is nothing for you, try again')
    else:
        #set the score for each film
        Score = []
        for i in range(len(Films)):
            # numerator and denominator
            Numerator = 0
            denominator = np.linalg.norm(Length[Films[i]][1])*np.linalg.norm(np.fromiter(Query_tfidf.values(), dtype = float))
            # dot product using Lenght dictionary 
            for j in range(len(Query)):
                if Vocabulary[Query[j]] in Length[Films[i]][0]:
                    Numerator += Query_tfidf[Vocabulary[Query[j]]]*Length[Films[i]][1][j]
            # evaluating the score
            Score.append(Numerator/denominator)
    
        Film_Score = dict(zip(Score, Films))
        
        # sort with the heap map
        heapSort(Score) 
        
        # save the dataframe
        df = output_second_score(Films, input_path, Score, Doc_Id_url, Film_Score)
        print(df)
    




    
if Choice == 3:
    # we star from the conjuntive query
    Films = conjuntive_query(Query, Inverted_index, Vocabulary, Docs)
    if len(Films) < k:
        k = len(Films) - 1
    
    composer = FILTER(composer)
    director = FILTER(director)
    
    
    #lets take the composer and the director
    Composers, Directors = search_composer_director(Films, input_path)
    
    # the score is based on the frequence of the words inside the documents
    freq = FREQ_value(Inverted_index, Vocabulary, Films)
    
    # if the user write sometring inside the director or the composer if the name compare inthe movie the score is 
    # If the user writes something in the section for the director and for the composer, for each word that matches the document the frequency count is increased by 25%
    #this is the counter of the matches
    counter_film = COUNT_value()
    
    # increasing the score
    Score_movie = FINAL_SCORE()
    if len(Films) != 0:
            
        Film_score = dict(zip(Score_movie, Films))
        
        # sort with the heap map
        heapSort(Score_movie) 
        
        # save the dataframe
        df = output_new_score(Films, input_path, Score_movie, Doc_Id_url, k, Film_score)
        print(df)
    pass

#df.loc[0].intro
    
    
# cars movie motors query
# Malcolm Dalglish music
# Frederick King Keller director
