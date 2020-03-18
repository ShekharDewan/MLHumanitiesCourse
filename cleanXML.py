import os
from pathlib import Path
from bs4 import BeautifulSoup as bs
from os import listdir
import shutil

def cleanTitle(title = ''):
    title = "_".join(title.split())
    titleTemp = ''.join(i for i in title if i.isdigit() or i.isalpha())
    title = titleTemp
    title = title.replace('?', '')
    return title

# Directories1000YearsGreek
# file_directories = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Directories1000YearsGreek.txt', 'r', encoding = 'UTF-8')
entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data')

#file_directories = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\DirectoriesPerseus.txt', 'r', encoding = 'UTF-8')
#directories = file_directories.readlines()



root = os.path.dirname(__file__)

    #directory = directory.replace('\n', '')
    #directory = os.path.normpath(directory)
    # print(directory)
    #path = Path(directory)
    

greekFiles = sorted(entries.rglob('*grc*.xml*'))
engFiles = sorted(entries.rglob('*eng*.xml*'))

os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus')
os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\Greek')
os.mkdir(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\English')
for f in greekFiles:
    title = title = (str(f).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    infile = open(f, 'r', encoding = 'UTF-8')
    contents = infile.read()
    soup = bs(contents,'xml')
    print('file = ', f)

    outName = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\Greek\\' + title +   '.xml'
    newFile = shutil.copy(f, outName)
    
    #outfile = open(
    #soup.prettify()
    
    #outfile.write(str(soup))
    #outfile.close()
    infile.close()
    
for f in engFiles:  
    title = title = (str(f).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    infile = open(f, 'r', encoding = 'UTF-8')
    contents = infile.read()
    soup = bs(contents,'xml')
    print('file = ', f)

    outName = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\English\\' + title +   '.xml'
    newFile = shutil.copy(f, outName)

    #outfile.write(str(soup))
    #outfile.close()
    infile.close()









    