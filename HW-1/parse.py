
from bs4 import BeautifulSoup
import csv
from parse_utils import PLOT, INTRO, DICT_INFOBOX, EMPTY_INFOBOX
import os.path



# read the html files from the HTML folder and save the tvs files inside the folder TSV
input_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/HTML'
output_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/TSV'


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
        with open(completeName_input, 'r', encoding="utf8") as out_file:
            page = out_file.read() 
        soup_i = BeautifulSoup(page, 'html5lib')
        
        # read all the paragraph
        all_p_i = soup_i.find_all('p')
       
        
        # for each possible name of the plot we do the follow loop
        no_plot = 0
        for k in possible_plots:
            try:
                # we are going to select the <h2> associated to the k-th name of the plot
                # if we find it we create the plot with the function PLOT inside collectop_utils.py
                tag_i = soup_i.select_one(k).find_parent('h2').find_next_sibling()
                plot = PLOT(tag_i, [])
                no_plot = 1
                break                         
            except:
                pass
        # if there is no plot we write 'NA'
        if no_plot == 0:
            plot = 'NA'
        # reading the intro: everything before the plot
        intro = INTRO(all_p_i,plot,[])    
        
        # try to read the infobox
        try: 
            # if we find it whe read it and save it as a dictionary into the result
            table = soup_i.find('table', class_='infobox vevent')
            result = DICT_INFOBOX(soup_i,{})
        except:
            # otherwise we save a dictionary with only 'NA' for each key
            result = EMPTY_INFOBOX()
        
        # we are going to create an array with only 0
        InfoFilm= [0]*14
        
        # saving the infobox
        for k in range(10):
            InfoFilm[k+4] = result.get(Name[k], 'NA')
        # saving the title
        InfoFilm[0] = soup_i.title.text[:-12]
        
        # saving the film_name
        try:
            InfoFilm[3] = table.find_all('tr')[0].text
        except:
            InfoFilm[3] = 'NA'
        
        # saving plot and intro
        InfoFilm[2] = ' '.join(plot)
        InfoFilm[1] = ' '.join(intro)
        
        # save the tsv file
        completeName_output = os.path.join(output_path, 'article_' + str(i) + '.tsv')
        
        with open(completeName_output, 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(InfoFilm)
        
    except:
        # if the html in empty, this mean that in collector there was the exception 404 so we save only 'NA' for each informations
        InfoFilm = ['NA']*14
        completeName_output = os.path.join(output_path, 'article_' + str(i) + '.tsv')
        with open(completeName_output, 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(InfoFilm)
        
        b.append(i)

    
    i += 1
















