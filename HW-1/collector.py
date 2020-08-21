from bs4 import BeautifulSoup
import requests
import time
import urllib.request, urllib.error, urllib.parse
from collector_utils import PRINT
import numpy as np
import pickle

############
# Inside the repository there are in the folder `data` pagese with 10000 `urls` each.
# The main of this file is to read all the `urls` and using bs4, from BeautifulSoup,
# save the whole page in a `html` format.
# 
# Is possible that some errors accurs during this process:
#   error 404 page not found:
#       In this case the page is dropped 
#   error 429 too many access: 
#       In this case there is a delay of 20 minutes   
#       (This error is avoided with the random delay between 1 and 5 seconds) 
############

# this is the pat for the general folder that contain everything
save_path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw3/'


# counter for the name of the file
counter = 0

# a list of all the empty pages
empty_file = []

# a dictionary with as key the Id of the document and value his url
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
        # save the url and the link
        Doc_Id_url[counter] = wiki_links[j].get('href')
        
        try:
            print(i,j,counter)
            
            # read the j-th page of wikipedia in the i-th HTML page of all links
            response = urllib.request.urlopen(wiki_links[j].get('href'))
            webContent = response.read().decode(response.headers.get_content_charset())
            
            # this function save this page in an .html file inside the folder at the address save_path+'HTML' 
            PRINT(save_path +'HTML', counter, webContent)
            # soup_i = BeautifulSoup(webContent, 'html5lib')
            
        # lets see the exceptions
        except urllib.error.HTTPError as e:
            # too many request so sleep for 20min and after save the last page
            if e.code == 429:
                time.sleep(20*60)
                response = urllib.request.urlopen(wiki_links[j].get('href'))
                webContent = response.read().decode(response.headers.get_content_charset())
                PRINT(save_path +'HTML', counter, webContent) 
            # page not found so save an html with the write 'NA'
            if e.code == 404:
                PRINT(save_path + 'HTML', counter, 'NA')
                empty_file.append(counter)
              
        
        counter += 1
        # random time sleep between 1 and 5 sec
        time.sleep(np.random.randint(1,6))
        

# save the dictionary as pkl
with open(save_path+'Doc_Id_url.pkl', 'wb') as fp:
    pickle.dump(Doc_Id_url, fp, protocol = pickle.HIGHEST_PROTOCOL)