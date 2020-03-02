import os
from pathlib import Path
import re
import shutil
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re


# C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data
p = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data')
wc = 0

i = 1

for currFile in p.rglob('*eng*.xml'):
    infile = open(currFile, 'r', encoding = 'UTF-8')
    contents = infile.read()
    soup = BeautifulSoup(contents,'lxml')

    try:
        text_tag = soup.find('text')
        for tag in text_tag.find_all(True):
            if (tag.name == 'note' or tag.name == 'reg' or tag.name == 'bibl' or tag.name == 'foreign'):
                    tag.decompose()
            else:
                pass
        text = text_tag.get_text()
        text = " ".join(text.split())
        text = text.strip('0123456789')
        if (i < 5):
            print(text.split(' '))
        i += 1
        for line in text:
            line = re.sub(r"(?<=[^\s])-(?=[^\s])", " @-@ ", line)
            line = line.replace(';', ' ;')
            line = line.replace('&', '&amp;')
            line = line.replace('quot ;', '&quot;')
            line = line.replace('?', ' ?')
            line = line.replace('.', ' . ')
            line = line.replace(',', ' ,')
            line = line.replace(':', ' :')
            line = line.replace("'", ' &apos; ')
            line = line.replace('(', '( ')
            line = line.replace(')', ' )')
            line = line.replace('/', ' / ')
            line = line.replace('[', '[ ')
            line = line.replace(']', ' ]')
            line = line.replace('!', ' !')
            line = line.replace('  ', ' ')
        words = text.split(' ')
        wc += len(text)
    except AttributeError:
        pass

print(wc)
