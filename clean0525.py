import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data\tlg0525\\')
outfileGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\CleanedData\tlg0525-001CleanedGreekXML', 'w', encoding = 'UTF-8')
outfileEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\CleanedData\tlg0525-001CleanedEnglishXML', 'w', encoding = 'UTF-8')

for currFile in sorted(entries.rglob('*grc*xml*')):
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        tags_to_keep_list = ['chapter', 'haeresis', 'verse', 'section', 'paragraph', 'p', 'placeName', 'name', 'seg', 'persName', 'quote']

        for division in divisions:
            subtype = division.get('subtype')
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
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
                # paragraph = paragraph.lstrip('0123456789')
                process = BeautifulSoup(paragraph, 'xml')
                tagsToRemove = process.find_all(['title'])
                for p in tagsToRemove:
                    p.extract()
                paragraph = str(process)
                
                outfileGrc.write(str(title) + "\t" + '\t' + str(chapter) + ":" + str(verse) + "\t" + text + '\n')
        outfileGrc.flush()
        os.fsync(outfileGrc.fileno())
    except AttributeError:
        pass
    infile.close()
outfileGrc.close()


for currFile in sorted(entries.rglob('*eng*xml*')):
    
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Current File Being Processed is: " + title)

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        for division in divisions:
            subtype = division.get('subtype')
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
                
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
                # paragraph = paragraph.lstrip('0123456789')
                outfileEng.write(str(title) + "\t" + '\t' + str(chapter) + ":" + str(verse) + "\t" + text + '\n')

        outfileEng.flush()
        os.fsync(outfileEng.fileno())
    except AttributeError:
        pass
    infile.close()
outfileEng.close()

