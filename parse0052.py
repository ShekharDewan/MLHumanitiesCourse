import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus')
outfileGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\tlg0059034GreekInput.txt', 'w', encoding = 'UTF-8')
outfileEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\tlg0059034EnglishOutput.txt', 'w', encoding = 'UTF-8')

outfileGrc.write("Book" + "\t" 'Version' "\t" + "Chapter" + ":" "Verse" + "\t" + "Greek Text" + "\n")
outfileEng.write("Book" + "\t" + 'Version' + '\t' "Chapter" + ":" "Verse" + "\t" + "Greek Text" + "\n")
grctitles = {'dummy' : 1}
engtitles = {'dummy' : 1}
version = 1

for currFile in sorted(entries.rglob('*grc*xml*')):
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)

    # title = (soup.find('title')).get_text()
    if title not in grctitles:
        grctitles[title] = 1
    else:
        grctitles[title] += 1
    version = grctitles[title]
    # title += str(grctitles[title])
    titlesGrc.write(title + '\t' + str(version) + '\n')

    # outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527_allXML_Cleaned' + '_output' + ".txt", 'w', encoding = 'UTF-8')

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        for division in divisions:
            subtype = division.get('subtype')
            # print("Hello")
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
                # print('hi')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
                
                for tag in division.find_all(True):
                    if (tag.name == 'div' or tag.name == 'chapter' or tag.name == 'haeresis' or tag.name == 'verse' or tag.name == 'section' or tag.name == 'paragraph' or tag.name == 'p' or tag.name == 'placeName' or tag.name == 'name' or tag.name == 'seg' or tag.name == 'persName' or tag.name == 'quote'):
                        # print(tag.name)
                        pass
                    else:
                        tag.decompose()
                # inside = subtype.find_all(True):

                '''
                for a in soup.find('a').children:
                    if isinstance(a,bs4.element.Tag):
                        a.decompose()
                '''

                # text = subtype.find(text=True, recursive=False)
                # text = ' '.join(subtype.find_all(text=True, recursive=False))
                # text = ' '.join(subtype.find(text=True, recursive=False) for subtype in soup.findAll(division.subtype))
                # text = division.get_text()
                text = division.get_text()
                text = " ".join(text.split())
                verse = division.get('n')
                #if(verse.isdigit()):
                paragraph = ""
                for para in division.stripped_strings:
                    paragraph += para

                paragraph = str(paragraph)
                # paragraph = (division.get_text()).strip()
                # paragraph = paragraph.replace('\t', ' ')
                # paragraph = paragraph.replace('\n', ' ')
                # paragraph = re.sub(r'\s([?.!"](?:\s|$))', r'\1', paragraph)
                
                paragraph = " ".join(paragraph.split())
                paragraph = paragraph.lstrip('0123456789')
                process = BeautifulSoup(paragraph, 'xml')
                tagsToRemove = process.find_all(['title'])
                for p in tagsToRemove:
                    p.extract()
                paragraph = str(process)
                
                outfileGrc.write(str(title) + "\t" + str(version) + '\t' + str(chapter) + ":" + str(verse) + "\t" + text + '\n')
        outfileGrc.flush()
        os.fsync(outfileGrc.fileno())
    except AttributeError:
        pass
    infile.close()
outfileGrc.close()
titlesGrc.close()




for currFile in sorted(entries.rglob('*eng*xml*')):
    
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Current File Being Processed is: " + title)
    # title = (soup.find('title')).get_text()
    if title not in engtitles:
        engtitles[title] = 1
    else:
        engtitles[title] += 1
    version = engtitles[title]
    titlesEng.write(title + '\t' + str(version) + '\n')

    # outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527_allxml_Cleaned' + '_output' + ".txt", 'w', encoding = 'UTF-8')
    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        for division in divisions:
            subtype = division.get('subtype')
            # print("Hello")
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
                # print('hi')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p' or 'seg'):
                
                for tag in division.find_all(True):
                    if (tag.name == 'div' or tag.name == 'chapter' or tag.name == 'haeresis' or tag.name == 'verse' or tag.name == 'section' or tag.name == 'paragraph' or tag.name == 'p' or tag.name == 'placeName' or tag.name == 'name' or tag.name == 'seg' or tag.name == 'persName' or tag.name == 'quote'):
                        # print(tag.name)
                        pass
                    else:
                        tag.decompose()
                text = division.get_text()
                text = " ".join(text.split())
                verse = division.get('n')
                #if(verse.isdigit()):
                paragraph = ""
                for para in division.stripped_strings:
                    paragraph += para

                paragraph = str(paragraph)
                # paragraph = (division.get_text()).strip()
                # paragraph = paragraph.replace('\t', ' ')
                # paragraph = paragraph.replace('\n', ' ')
                # paragraph = re.sub(r'\s([?.!"](?:\s|$))', r'\1', paragraph)
                
                paragraph = " ".join(paragraph.split())
                paragraph = paragraph.lstrip('0123456789')
                outfileEng.write(str(title) + "\t" + str(version) + '\t' + str(chapter) + ":" + str(verse) + "\t" + text + '\n')

        outfileEng.flush()
        os.fsync(outfileEng.fileno())
    except AttributeError:
        pass
    infile.close()
outfileEng.close()
titlesEng.close()

