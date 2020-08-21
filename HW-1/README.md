# HW-1

**Goal of the homework**: *Build a search engine over a list of movies that have a dedicated page on Wikipedia.*


## 1. Data collection

For this homework, there is no provided dataset, but we have to build our own. The data collection task is divided into **three** subtasks.



### 1.1. Get the list of movies

In the folder `data`, inside this [repository](https://github.com/CriMenghini/ADM/tree/master/2019/Homework_3), there are several html pages. Opening one of them is possible see a list of `urls` of Wikipedia pages, and each one of them refers to a specific movie.

The first subtask is to **parse** the `html` page and **get** the complete list of `urls`.

### 1.2. Crawl Wikipedia

At this point, you obtained *n* different lists of `urls`. Now we want you to go inside each one of this `url`, and to crawl specific informations from them. 
Each crawled page is saved with the name `article_i.html`, where `i` corresponds to the number of articles you have already downloaded. 

### 1.3 Parse downloaded pages

Now that all the movies' Wikipedia pages are stored, it is time to parse them and extract the information of interest.

For each Wikipedia Page we took:

1. Title
2. First two sections of the article. Refer to them respectively as `intro` and `plot`.

3. The following informations from the **infobox**: film_name, director, producer, writer, starring, music, release date, runtime, country, language, budget.

Those info has to be saved into different `.tsv` files of this structure:

```
title \t intro \t plot \t info_1 \t info_2 \t info_3 \t info_4 ... \t info_n
```

__Example__:

```
title \t ... \t  director \t language 
    
harry potter \t ... \t jojo \t english
```

## 2. Search Engine

Now, we want to create two different Search Engines that, given as input a query, return the movies that match the query.

As a first common step, we have to preprocess the documents by

1. Removing stopwords
2. Removing punctuation
3. Stemming

For this purpose, we used the [nltk library](https://www.nltk.org/).

### 2.1. Conjunctive query
At this moment, we narrow our interest on the `intro` and `plot` of each document. It means that the first Search Engine will evaluate queries with respect to the aforementioned information.

#### 2.1.1) Create your index!

The first brick of this homework is to create the Inverted Index. It will be a dictionary of this format:

```
{
term_id_1:[document_1, document_2, document_4],
term_id_2:[document_1, document_3, document_5, document_6],
...}
```
where _document\_i_ is the *id* of a document that contains the word.


#### 2.1.2) Execute the query
Given a query, that you let the user enter:

```
disney movies 2019
```

the Search Engine will return a list of documents.

##### What documents do we want?
Since we are dealing with conjunctive queries (AND), each of the returned documents should contain all the words in the query.
The final output of the query return, if present, the following information for each of the selected documents:

* Title
* Intro
* Url

__Example Output__:

| Title | Intro | Wikipedia Url |
|:-----------------------------:|:-----:|:-----------------------------------------------------------:|
| Toy Story 4 | ... | https://en.wikipedia.org/wiki/Toy_Story_4 |
| The Lion King | ... | https://en.wikipedia.org/wiki/The_Lion_King_(2019_film) |
| Dumbo | ... | https://en.wikipedia.org/wiki/Dumbo_(2019_film) |




### 2.2) Conjunctive query & Ranking score

In the new Search Engine, given a query, we want to get the *top-k* documents related to the query. In particular:

* Find all the documents that contains all the words in the query.
* Sort them by their similarity with the query
* Return in output *k* documents, or all the documents with non-zero similarity with the query when the results are less than _k_. we used a heap data structure (you can use Python libraries) for maintaining the *top-k* documents.

To solve this task, we used the *tfIdf* score, and the _Cosine similarity_. Let's see how.


#### 2.2.1) Inverted index
Your second Inverted Index is of this format:

```
{
term_id_1:[(document1, tfIdf_{term,document1}), (document2, tfIdf_{term,document2}), (document4, tfIdf_{term,document4}), ...],
term_id_2:[(document1, tfIdf_{term,document1}), (document3, tfIdf_{term,document3}), (document5, tfIdf_{term,document5}), (document6, tfIdf_{term,document6}), ...],
...}
```

Practically, for each word there is the list of documents in which it is contained in, and the relative *tfIdf* score.


#### 2.2.2) Execute the query

Once you get the right set of documents, we want to know which are the most similar according to the query. For this purpose, as scoring function we will use the Cosine Similarity with respect to the *tfIdf* representations of the documents.

Given a query, that you let the user enter:
```
disney movies 2019
```
the Search Engine return a list of documents, __ranked__ by their Cosine Similarity with respect to the query entered in input.

More precisely, the output must contain:
* Title
* Intro
* Url
* The similarity score of the documents with respect to the query


__Example Output__:

| Title | Intro | Wikipedia Url | Similarity |
|:-------------:|:-----:|:-------------------------------------------------------:|------------|
| Toy Story 4 | ... | https://en.wikipedia.org/wiki/Toy_Story_4 | 0.96 |
| The Lion King | ... | https://en.wikipedia.org/wiki/The_Lion_King_(2019_film) | 0.92 |
| Dumbo | ... | https://en.wikipedia.org/wiki/Dumbo_(2019_film) | 0.87 |

## 3. Define a new score!

This score gives the user the possibility to search for a movie both on the basis of the words but also on the basis of the director and the composer. Each match in these categories increases that movie's score by 25%, is possible choose the number of results that we want see. For the sorting algorithm we are going to use the heapsort.

## 4. Algorithmic question

You are given a string, *s*. Let's define a subsequence as the subset of characters that respects the order we find them in *s*. For instance, a subsequence of "DATAMINING" is "TMNN". Your goal is to **define and implement** an algorithm that finds the length of the longest possible subsequence that can be read in the same way forward and backwards. For example, given the string "DATAMININGSAPIENZA" the answer should be 7 (d**A**tam**ININ**gsap**I**enz**A**).




# CODE FILEs

## collector.py

Inside the repository there are in the folder `data` pagese with 10000 `urls` each. The main of this file is to read all the `urls` and using bs4, from BeautifulSoup, save the whole page in a `html` format. 

Is possible that some errors accurs during this process:
  * error 404 page not found:
      In this case the page is dropped 
  * error 429 too many access: 
      In this case there is a delay of 20 minutes   
      (This error is avoided with the random delay between 1 and 5 seconds) 

## collector_utils.py

This file contain the function that save the webContent of the page inside the save_path with the name article_counter.html

## parse.py

This python code contains the lines of code needed to parse the entire collection of html pages and save those in tsv files. Using bs4, from BeautifulSoup, is possible read process the html file and estract:
Title, Intro, Plot, Film_name, Director, Producer, Writer, Starring, Music, Release date, Runtime, Country, Language and Budget.

The output of each html is a tsv file with all the infos

## parse_utils.py

This file contains all the functions used in parse.py

## index.py

This python code allow to process both intro and plot in order to build the inverted index the words->numbers map and a dictionary with the size of each document.  

Each document is preprocess in order to:
  * Removing stopwords (e.g.  and, or, the.....)
  * Removing punctuation
  * Stemming (i.e. all these words 'Playing','Plays','Played' became 'Play')
   
After the this cleaning process is possible create the directed index, a dictionary of the same form of the inverted index but with the frequency of the words indide the document insted of tf-idf.

At the end we can calculate the tf-idf and create the inverted index taking care to map the words into numbers, to save memory.


## index_utils.py

This python code contains all the unction for index.py


## main.py

This file is the file with the code to run all the three Search Engines.
It is divided in 5 parts:
  * Search engine 1 (conjunctive queries): 
      Each of the returned documents should contain all the words in the query. The final output of the query must return, if present, Title, Intro and URL
       
  * Search engine 2 (Conjunctive query & Ranking score): 
      Once we get the right set of documents, we want to know which are the most similar according to the query. For this purpose, as scoring function we will use the Cosine similarity with respect to the tf-idf representations of the documents.
  
  * Search engine 3 (our score):
      This score gives the user the possibility to search for a movie both on the basis of the words but also on the basis of the director and the composer. Each match in these categories increases that movie's score by 25%, is possible choose the number of results that we want see. For the sorting algorithm we are going to use the heapsort
  
  * Importing dictionaries:
      save in memory the inverted index, the vocabulary ant the match between doc_id and URL

  * Interactive part:
      It is a piece of code that allow the user to choose the type of search engine, the number of results and insert all the words.

## exercise_4.py

This is the part for the theorical question

## main.ipynb

A jupiter notebook with all the code