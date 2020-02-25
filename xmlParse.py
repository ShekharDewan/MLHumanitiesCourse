'''

import xml.etree.ElementTree as ET

text = open('Perseus_clean.xml', encoding='UTF-8')
# text = open('tlg0527.tlg001.opp-grc2.xml')
# tlg0527.tlg001.opp-grc2.xml

tree = ET.parse(text)
root = tree.getroot()
print(root)

#file = open("testfile.txt", "w")
file = open("genesis.txt", "w", encoding='UTF-8')

file.write("Book" + "\t" + "Chapter" + ":" "Verse" + "\t" + "English Text" + "\n")
# file.write("\n")
for child in root.findall('text'):
    for body in child.findall('div1'):
        for chapter in body.findall('div2'):
            for p in chapter.findall('p'):
                i = 1
                for text in p.itertext():
                    text = text.replace('\t', ' ')
                    text = text.replace('\n', ' ')
                    text = " ".join(text.split())
                    file.write(body.attrib["n"] + "\t" + chapter.attrib["n"] + ":" + str(i) + "\t" + text + "\n")
                    i = i + 1

file.close()
'''

# import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
# from pathlib import Path
import re

# entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus_clean.xml')
outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus_output.txt', 'w', encoding = 'UTF-8')
# outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\output.txt', 'a+', encoding = 'UTF-8')
outfile.write("Book" + "\t" + "Chapter" + ":" "Verse" + "\t" + "Greek Text" + "\n")

# for currFile in entries.iterdir():
# print ("Current File Being Processed is: " + str(currFile))
infile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus_clean.xml', 'r', encoding = 'UTF-8')

contents = infile.read()
soup = BeautifulSoup(contents,'xml')
title = (soup.find('title')).get_text()
print('Title:', title)

# outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527_allXML_Cleaned' + '_output' + ".txt", 'w', encoding = 'UTF-8')

text = soup.find_all('text')
for child in text:
    for body in child.find_all('div1'):
        for chapter in body.find_all('div2'):
            verse = 1
            stuff = chapter.descendants
            for st in stuff:
                if st.name == 'milestone':
                    verse = st
                else:
                    st =  " ".join(str(st).split())
                    print(body['n'] + '\t' + chapter['n'] + ':' + str(verse) + '\t' + str(st))
            #print(stuff.findChildren('n', recursive = False)) #.find_all['n'])
                # print(descent)

'''            
for para in chapter.find_all('p'):
                for p in para.itertext():
                    outfile.write(file.write(body.attrib["n"] + "\t" + chapter.attrib["n"] + ":" +  + "\t" + " ".join(text.split()) + "\n"))
divisions = text.find_all('div1')
chapter = 1
verse = 1
for division in divisions:
    subtype = division.get('subtype')
    if(subtype == 'chapter'):
        chapter = division.get('n')
    if(subtype == 'verse' or subtype == 'section'):
        verse = division.get('n')
        for paragraph in division.stripped_strings:
            # paragraph = (division.get_text()).strip()
            # paragraph = paragraph.replace('\t', ' ')
            # paragraph = paragraph.replace('\n', ' ')
            paragraph = " ".join(paragraph.split())
            outfile.write(str(title) + "\t" + str(chapter) + ":" + str(verse) + "\t" + paragraph + '\n')
        
        paragraph = division.descendants
        i = 0
        for para in paragraph:
            if (i == 1):
                try:
                    for stripped in para.stripped_strings:
                        outfile.write(str(title) + "\t" + str(chapter) + ":" + str(verse) + "\t" + (stripped).replace('\n','') + '\n')
                except AttributeError:
                        outfile.write(str(title) + "\t" + str(chapter) + ":" + str(verse) + "\t" + (para).replace('\n','') + '\n')
                
            i += 1
        '''
outfile.flush()
os.fsync(outfile.fileno())
infile.close()
outfile.close()