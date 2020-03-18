import os
from pathlib import Path
from bs4 import BeautifulSoup as bs
from os import listdir
import shutil

'''
This program moves xml documents for a nested directory structure into two folders within Perseus - 
English and Greek for the pertinent texts. 
Currently does greek and english one after the other - this can be improved with zip. 
'''

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data')

root = os.path.dirname(__file__)    

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
    infile.close()









    