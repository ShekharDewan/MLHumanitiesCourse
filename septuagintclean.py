from bs4 import BeautifulSoup as bs
from bs4 import NavigableString
import re

from pathlib import Path
# text = open('Perseus_clean.xml')

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527_allXML')
i = 0
for currFile in entries.iterdir():
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = bs(contents,'xml')
    title = (soup.find('title')).get_text()
    print(title)

    outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527' + '_' + title + '_cleaned' '.xml', 'w', encoding = 'UTF-8')
    # soup = bs(infile, 'lxml')
    soup.prettify()
    pn = soup.find_all(["note", "lb", "milestone", "pb", 'head'])

    for p in pn:
        p.extract()

    soup

    invalid_tags = ['lb', 'l', 'lg', 'p']
    for tag in invalid_tags: 
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    
    outfile.write(str(soup))
    outfile.close()
    infile.close()



# text = open('tlg0527.tlg001.opp-grc2.xml', encoding = "UTF-8")
# text = open('Perseus_text_1999.01.0156.xml')
# cleanp = open("tlg0527.tlg001.opp-grc2_clean.xml", "w", encoding = "UTF-8")

