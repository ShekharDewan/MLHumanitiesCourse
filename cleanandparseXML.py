import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

greek_entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\Greek')
english_entries = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus\English')

#tags_to_remove_english = ['note', 'bibl']
#tags_to_remove_greek = ['bibl', ]
#tags_to_keep_english = ['chapter', 'haeresis', 'verse', 'section', 'paragraph', 'p', 'placeName', 'name', 'seg', 'persName', 'quote']
#tags_to_keep_greek = ['note']

'''
Program for cleaning and parsing english and greek xml texts from the perseus project. Currently does greek and then english - 
this could be improved by using sort and then zip, and then to do it all together, making the code much shorter. 
'''


for currFile in sorted(greek_entries.rglob('*xml*')):
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)

    outfileGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\\' + title + 'GRC.txt', 'w', encoding = 'UTF-8')
    outfileGrc.write("title" + '\t' + 'Book' + "\t" + "Chapter" + ":" "Verse" + "\t" + "Greek Text" + "\n")
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        book = 1
        chapter = 1
        verse = 1
        for division in divisions:
            if(division.get('type') == 'edition'):
                pass
            else:
                
                subtype = division.get('subtype')
                if(subtype == 'book'):
                    if(division.get('n') != None):
                        book = division.get('n')
                else:
                    if(subtype == 'chapter' or subtype == 'haeresis'):
                        if(division.get('n') != None):
                            chapter = division.get('n')
                    if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
                        
                        tags_to_keep_list = ['chapter', 'haeresis', 'verse', 'section', 'paragraph', 'p', 'placeName', 'name', 'seg', 'persName', 'quote']
                        for tag in division.find_all(True):
                            if (tag.name == 'div' or tag.name == 'chapter' or tag.name == 'haeresis' or tag.name == 'verse' or tag.name == 'section' or tag.name == 'paragraph' or tag.name == 'p' or tag.name == 'placeName' or tag.name == 'name' or tag.name == 'seg' or tag.name == 'persName' or tag.name == 'quote'):
                                pass
                            else:
                                tag.decompose()

                        text = division.get_text()
                        text = " ".join(text.split())
                        verse = division.get('n')
                        
                        paragraph = ""
                        for para in division.stripped_strings:
                            paragraph += para

                        paragraph = str(paragraph)                    
                        paragraph = " ".join(paragraph.split())
                    
                        outfileGrc.write(str(title) + '\t' + str(book) + '\t' + str(chapter) + ":" + str(verse) + "\t" + paragraph + '\n')
        outfileGrc.flush()
        os.fsync(outfileGrc.fileno())
    except AttributeError:
        pass
    infile.close()
    outfileGrc.close()



for currFile in sorted(english_entries.rglob('*xml*')):
    engtitles = {'dummy' : 1}
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Current File Being Processed is: " + title)
    # title = (soup.find('title')).get_text()
    outfileEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\\' + title + 'ENG.txt', 'w', encoding = 'UTF-8')
    outfileEng.write("title" + '\t' + 'Book' + "\t" + "Chapter" + ":" "Verse" + "\t" + "English Text" + "\n")
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        book = 1
        chapter = 1
        verse = 1
        for division in divisions:
            if(division.get('type') == 'edition'):
                pass
            else:
                subtype = division.get('subtype')
                if(subtype == 'book'):
                    if(division.get('n') != None):
                        book = division.get('n')
                else:
                    if(subtype == 'chapter' or subtype == 'haeresis'):
                        if(division.get('n') != None):
                            chapter = division.get('n')
                    if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
                        
                        tags_to_keep_list = ['chapter', 'haeresis', 'verse', 'section', 'paragraph', 'p', 'placeName', 'name', 'seg', 'persName', 'quote']
                        for tag in division.find_all(True):
                            if (tag.name == 'div' or tag.name == 'chapter' or tag.name == 'haeresis' or tag.name == 'verse' or tag.name == 'section' or tag.name == 'paragraph' or tag.name == 'p' or tag.name == 'placeName' or tag.name == 'name' or tag.name == 'seg' or tag.name == 'persName' or tag.name == 'quote'):
                                pass
                            else:
                                tag.decompose()

                        text = division.get_text()
                        text = " ".join(text.split())
                        verse = division.get('n')
                        paragraph = ""
                        for para in division.stripped_strings:
                            paragraph += para

                        paragraph = str(paragraph)                    
                        paragraph = " ".join(paragraph.split())

                        outfileEng.write(str(title) + '\t' + str(book) + '\t' + str(chapter) + ":" + str(verse) + "\t" + paragraph + '\n')

        outfileEng.flush()
        os.fsync(outfileEng.fileno())
    except AttributeError:
        pass
    infile.close()
    outfileEng.close()

