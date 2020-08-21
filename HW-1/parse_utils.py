


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


def DICT_INFOBOX(soup_i,result):
    # we read the infobox and make a dictionary
    table = soup_i.find('table', class_='infobox vevent')
    for tr in table.find_all('tr'):
        if tr.find('th'):
            result[tr.find('th').text] = tr.get_text(strip=True, separator=" ")[len(tr.find('th').text):]#[m.text for m in tr.find_all('td')]#[len(tr.find('th')):]
        else:
            pass
    return result

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






