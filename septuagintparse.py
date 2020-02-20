import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

# entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\Perseus')
# outfileGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\PerseusGreekInput.txt', 'w', encoding = 'UTF-8')
# outfileEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\PerseusEnglishOutput.txt', 'w', encoding = 'UTF-8')
# titlesGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\PerseusGreekTitles.txt', 'w', encoding = 'UTF-8')
# titlesEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\PerseusEnglishTitles.txt', 'w', encoding = 'UTF-8')

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\ThousandYearsCleaned')
outfileGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\Greek1000YearsGreekInput.txt', 'w', encoding = 'UTF-8')
outfileEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\Greek1000YearsEnglishOutput.txt', 'w', encoding = 'UTF-8')
titlesGrc = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\Greek1000YearTitles.txt', 'w', encoding = 'UTF-8')
titlesEng = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\TrainingData\English1000YearTitles.txt', 'w', encoding = 'UTF-8')

# outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\output.txt', 'a+', encoding = 'UTF-8')
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
    
    title = (soup.find('title')).get_text()
    if title not in grctitles:
        grctitles[title] = 1
    else:
        grctitles[title] += 1
    version = grctitles[title]
    # title += str(grctitles[title])
    titlesGrc.write(title + '\t' + str(version) + '\n')

    # outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\tlg0527_allXML_Cleaned' + '_output' + ".txt", 'w', encoding = 'UTF-8')

    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        for division in divisions:
            subtype = division.get('subtype')
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p'):
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
                process = BeautifulSoup(paragraph, 'lxml')
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
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')
    title = (soup.find('title')).get_text()
    if title not in engtitles:
        engtitles[title] = 1
    else:
        engtitles[title] += 1
    version = engtitles[title]
    titlesEng.write(title + '\t' + str(version) + '\n')

    # outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\ML for the Humanities\tlg0527_allXML_Cleaned' + '_output' + ".txt", 'w', encoding = 'UTF-8')
    try:
        text = soup.find('text')
        divisions = text.find_all('div')
        chapter = 1
        verse = 1
        for division in divisions:
            subtype = division.get('subtype')
            if(subtype == 'chapter' or subtype == 'haeresis'):
                chapter = division.get('n')
            if(subtype == 'verse' or subtype == 'section' or 'paragraph' or 'p'):
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

