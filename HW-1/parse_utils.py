
############
# This file contains all the functions used in parse.py
############



############
# This function take as imput a <h2> and an empty list.
# The plot is made up of all the paragraphs between the first twu <h2>; of course 
# is possible that after the plot there is nothing so we have to make an exception 
############

def PLOT(tag_i, plot):
    # from the <h2> until there is a new <h2> we take all the plots
    try:
        while True:
            if tag_i.name == 'h2':
                return plot
            if tag_i.name == 'p':
                plot.append(tag_i.text[:-2].replace('\n', ''))
            tag_i = tag_i.find_next_sibling()
    except: 
        # it's for pages that have nothing after the polt
        pass
    return plot


############
# The introduction is nothing more than all the paragraphs before the plot, so
# we compare all the paragraph with the first p of the plot till there is a match
############


def INTRO(all_p_i,plot,intro):
    # if plot in empty we try to save the first paragraph, otherwise we save 'NA'
    if plot=='NA':
        try:
            return all_p_i[0][-2]
        except:
            return 'NA'
    #select all the paragraph writen before the plot
    else:
        for par in all_p_i:
            if par.text[:-2].replace('\n', '') == plot[0]:
                break
            else:
                intro.append(par.text.replace('\n', ''))
    return intro

############
# This function read all the infos inside the infobox and return a dictionary
############

def DICT_INFOBOX(soup_i,result):
    # we read the infobox and make a dictionary
    table = soup_i.find('table', class_='infobox vevent')
    for tr in table.find_all('tr'):
        if tr.find('th'):
            result[tr.find('th').text] = tr.get_text(strip=True, separator=" ")[len(tr.find('th').text):]
        else:
            pass
    return result


############
# If there isn't an infobox we create an empty one
############
def EMPTY_INFOBOX():
    # if there is not the infobox we save a dictionary with only 'NA' for each key
    a = {'Directed by': 'NA',
             'Produced by': 'NA',
             'Written by': 'NA',
             'Starring': 'NA',
             'Music by': 'NA',
             'Release date': 'NA',
             'Running time': 'NA',
             'Country': 'NA',
             'Language': 'NA',
             'Budget': 'NA'}
    return a






