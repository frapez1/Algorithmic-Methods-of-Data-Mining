'''
from bs4 import BeautifulSoup
import requests
import time
import urllib.request, urllib.error, urllib.parse
from collector_utils import PRINT
import numpy as np
import pickle
import os.path

# where we want save all the html files
save_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'
input_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'


# counter for the name of the file
counter = 0

# a list of all the empty pages
empty_file = []

Doc_Id_url = {}

# A loop for each list of link
for i in range(1,4):
    
    # We are reading the HTML with all the links for the pages of wikipedia
    list_of_pages = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies' + str(i) + '.html'               
    request = requests.get(list_of_pages )
    
    
    # we parse this file 
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # we create a list with all the links
    wiki_links = soup.select('a')
    
    N = len(wiki_links)
    for j in range(0,N):
        print(counter)
            

        completeName_output = os.path.join(input_path, 'article_' + str(counter) + '.tsv')
        with open(completeName_output, 'r') as input_file:
            intro_plot = input_file.readline()
        
        Doc_Id_url[counter] = {intro_plot[0] : wiki_links[j].get('href')}
        
        counter += 1
        # andom time sleep between 1 and 5 sec

file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'

# save the 3 dictionary as pkl
with open(file+'Doc_Id_url.pkl', 'wb') as fp:
    pickle.dump(Doc_Id_url, fp, protocol = pickle.HIGHEST_PROTOCOL)
    
    
    
    
    
    
    
    
'''


'''


from bs4 import BeautifulSoup
import csv
from parse_utils import PLOT, INTRO, DICT_INFOBOX, EMPTY_INFOBOX
import os.path
import pickle



file = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'

with open(file + 'Doc_Id_url.pkl', 'rb') as fp:
    Doc_Id_url = pickle.load(fp)


# read the html files from the HTML folder and save the tvs files inside the folder TSV
input_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'
output_path = '/home/lex/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'


# how wiki call the plot section
possible_plots = ['#Plot','#Plot_summary', '#Premise']
     
# how save informatrions into the tsv files                  
infos = ['title', 'intro', 'plot' ,'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']

# what wiki write inside the infobox
Name = ['Directed by', 'Produced by', 'Written by', 'Starring', 'Music by', 'Release date', 'Running time', 'Country', 'Language', 'Budget']

# the list of all the empty html page
b = []


# read file from i up to N
N = 30000
i = 0


while i < N:
    print(i)
    # select the html file
    completeName_input = os.path.join(input_path, 'article_' + str(i) + '.html')
    try:
        
        # open that file
        with open(completeName_input, 'r') as out_file:
            page = out_file.read() 
    
        soup_i = BeautifulSoup(page, 'html5lib')
        
        # read all the paragraph
    
        
        # for each possible name of the plot we do the follow loop
        
        # we are going to create an array with only 0
        #InfoFilm= [0]
        
        # saving the infobox
        
        #InfoFilm[0] = soup_i.title.text[:-12]
        
        # saving the film_name
        Doc_Id_url[i] = {soup_i.title.text[:-12] : Doc_Id_url[i]}
        
    except:
        # if the html in empty, this mean that in collector there was the exception 404 so we save only 'NA' for each informations
        
        Doc_Id_url[i] = {'NA' : Doc_Id_url[i]}
    
    i += 1


# save the dictionary as pkl
with open(file+'Doc_Id_url.pkl', 'wb') as fp:
    pickle.dump(Doc_Id_url, fp, protocol = pickle.HIGHEST_PROTOCOL)


'''


import os.path
import pickle



file = 'C:/Users/franc/Desktop//Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'

with open(file + 'Doc_Id_url.pkl', 'rb') as fp:
    Doc_Id_url = pickle.load(fp)


# we read the tsv files from the folder TSV 
input_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'

Doc_Id_title_url= {}


N = 30000
i = 0
while i < N:
    print(i)
    # read the i-th tsv
    completeName_input = os.path.join(input_path, 'article_' + str(i) + '.tsv')
    with open(completeName_input, 'r') as input_file:
        intro_plot = input_file.readline()
    # select only the intro and the plot
    intro_plot = intro_plot.split('\t')[0]
    Doc_Id_title_url[i] = {intro_plot : Doc_Id_url[i]}

    i+=1


# save the dictionary as pkl
with open(file+'Doc_Id_title_url.pkl', 'wb') as fp:
    pickle.dump(Doc_Id_title_url, fp, protocol = pickle.HIGHEST_PROTOCOL)


































