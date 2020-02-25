import os
from pathlib import Path
import re

# C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data
p = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\canonical-greekLit-master\data')
outfile = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\DirectoriesPerseus.txt', 'w', encoding = 'UTF-8')

for filename in p.rglob('*eng*.xml'):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, filename)
    dir_path = os.path.dirname(os.path.realpath(abs_file_path))
       
    outfile.write(dir_path + '\n')
    outfile.flush()
    os.fsync(outfile.fileno())

outfile.close()
