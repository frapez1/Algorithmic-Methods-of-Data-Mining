import os.path

def PRINT(save_path, counter, webContent):
    # We are going to create an .html file into the folder with the page
    completeName = os.path.join(save_path, 'article_' + str(counter) + '.html')
    with open(completeName, 'w') as out_file:
        out_file.write(str(webContent))
    return