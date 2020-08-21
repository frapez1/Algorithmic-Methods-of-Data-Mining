import os.path


############
# This file contain the function that save the webContent of the page inside the 
# save_path with the name article_counter.html
############



def PRINT(save_path, counter, webContent):
    # We are going to create an .html file into the folder with the page
    completeName = os.path.join(save_path, 'article_' + str(counter) + '.html')
    with open(completeName, 'w') as out_file:
        out_file.write(str(webContent))
    return