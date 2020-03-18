import os
from pathlib import Path
import re
import shutil

entries  = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\MatchedTitledTrainingData')
outpath = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\CleanedData\\'
for f in sorted(entries.rglob('*')):
    if os.path.getsize(f) > 200 * 1024:
        outName = str(outpath + str(str(f).split('\\')[-1]) + '.xml')
        shutil.copy(f, outName)
