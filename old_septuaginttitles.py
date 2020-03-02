import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\tlg0527_allXML_Cleaned')
outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\titles.txt', 'w', encoding = 'UTF-8')
# outfile.write("Book" + "\t" + "Chapter" + "\t" "Verse" + "\t" + "Greek Text" + "\n")


for currFile in entries.iterdir():
    print ("Current File Being Processed is: " + str(currFile))
    infile = open(currFile, 'r', encoding = 'UTF-8')

    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    title = (soup.find('title')).get_text()
    outfile.write(title + '\n')

    outfile.flush()
    os.fsync(outfile.fileno())
    infile.close()