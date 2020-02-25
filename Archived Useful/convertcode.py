import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from pathlib import Path
import re

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse')
replacement = 'MLHumanitiesCourse'
for fname in sorted(entries.rglob('*.py*')):
    fpath = os.path.join(entries, fname)
    with open(fpath, encoding = 'utf-8') as f:
        s = f.read()
    s = s.replace("MLHumanitiesCourse", replacement)
    with open(fpath, "w") as f:
        f.write(s)

        