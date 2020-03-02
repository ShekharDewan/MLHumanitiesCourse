import os
from pathlib import Path
from bs4 import BeautifulSoup as bs
from os import listdir

def cleanTitle(title = ''):
    title = "_".join(title.split())
    titleTemp = ''.join(i for i in title if i.isdigit() or i.isalpha())
    title = titleTemp
    title = title.replace('?', '')
    return title

# Directories1000YearsGreek
# file_directories = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Directories1000YearsGreek.txt', 'r', encoding = 'UTF-8')
file_directories = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\DirectoriesPerseus.txt', 'r', encoding = 'UTF-8')
directories = file_directories.readlines()



root = os.path.dirname(__file__)

for directory in directories:    
    directory = directory.replace('\n', '')
    directory = os.path.normpath(directory)
    # print(directory)
    path = Path(directory)
    greekFiles = path.rglob('*grc*.xml*')
    engFiles = path.rglob('*eng*.xml*')
    # os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus')
    # os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\Greek')
    # os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\English')
    for f in greekFiles:
        infile = open(f, 'r', encoding = 'UTF-8')
        contents = infile.read()
        soup = bs(contents,'xml')
        print('file = ', f)

        outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\\' + os.path.basename(g) +   '.xml', 'w', encoding = 'UTF-8')
        soup.prettify()
        
        outfile.write(str(soup))
        outfile.close()
        infile.close()
        
    for f in engFiles:
        infile = open(f, 'r', encoding = 'UTF-8')
        contents = infile.read()
        soup = bs(contents,'xml')
        print('file = ', f)

        outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\\' + os.path.basename(e) + '.xml', 'w', encoding = 'UTF-8')
        soup.prettify()

        '''
        tagsToRemove = soup.find_all(["note", "lb", "milestone", "pb", 'head', 'foreign', 'gap', 'del'])

        for p in tagsToRemove:
            p.extract()

        soup

        invalid_tags = ['lb', 'l', 'lg', 'p']
        for tag in invalid_tags: 
            for match in soup.findAll(tag):
                match.replaceWithChildren()
        '''

        outfile.write(str(soup))
        outfile.close()
        infile.close()









    