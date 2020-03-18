import os
from pathlib import Path
import re
import shutil

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\Perseus')

engTitles = set()
grcTitles = set()
for currFile in sorted(entries.rglob('*grc*xml*')):
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)
    engTitles.add(title)

for currFile in sorted(entries.rglob('*eng*xml*')):
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)
    grcTitles.add(title)

titlesToDrop = engTitles.union(grcTitles) - engTitles.intersection(grcTitles)

for currFile in sorted(entries.rglob('*xml*')):
    title = (str(currFile).split('\\'))[-1] 
    title = title.split('.')[0] + "" + title.split('.')[1]
    print ("Title is: " + title)
    if(title in titlesToDrop):
        os.remove(currFile) 