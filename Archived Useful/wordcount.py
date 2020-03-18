import os
from pathlib import Path
import re
import shutil
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re



'''
Counts the number of words in the text of a folder containing XML files from the Perseus project.
'''
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
        # text = text.strip('.')
       
        tokenized_text = ''
        #for text in text:
        text = re.sub(r"(?<=[^\s])-(?=[^\s])", " @-@ ", text)
        text = text.replace(';', ' ;')
        text = text.replace('&', '&amp;')
        text = text.replace('quot ;', '&quot;')
        text = text.replace('?', ' ?')
        text = text.replace('.', ' . ')
        text = text.replace(',', ' ,')
        text = text.replace(':', ' :')
        text = text.replace("'", ' &apos; ')
        text = text.replace('(', '( ')
        text = text.replace(')', ' )')
        text = text.replace('/', ' / ')
        text = text.replace('[', '[ ')
        text = text.replace(']', ' ]')
        text = text.replace('!', ' !')
        text = text.replace('  ', ' ')
        tokenized_text += text
        words = tokenized_text.split(' ')
        if (i < 5):
            print(words)
        else:
            pass #print('hi')
        i += 1
        wc += len(words)
    except AttributeError:
        pass

print(int(wc))
