import sys
import csv
import os
from pathlib import Path
csv.field_size_limit(100000000)
max_field_size = 100000
no_period_field_size = 1000

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def make_dict_from_tsv_file(filestring):
	text_for_citation = dict()
	with open(filestring, newline='\n', encoding = 'UTF-8') as tsv_file:
		reader = csv.reader(tsv_file, quoting=csv.QUOTE_NONE, delimiter='\t')
		for line in reader:
			try:
				if(len(line[1]) < max_field_size):
					text_for_citation[line[0]] = line[1]
			except Exception as e:
				pass
	return text_for_citation


entries = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\MatchedTitledPeriodTrainingData')
greek_input = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\\' + 'InputGreek.txt'
english_output = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\\' + 'OutputEnglish.txt'
greek_save = open(greek_input, 'w', encoding = 'utf-8')
eng_save = open(english_output, 'w', encoding = 'utf-8')
for grc_file in sorted(entries.rglob('*GRC*')):
    title = (str(grc_file).split('\\'))[-1]
    title = title.split('GRC')[0]
    eng_file = ''
    #Find corresponding english, and eliminate if it doesn't exist. 
    for f in sorted(entries.rglob('*ENG*')):
        title_eng = (str(f).split('\\'))[-1]
        title_eng = title_eng.split('ENG')[0]
        if(title == title_eng):
            eng_file = f
            break
    if(eng_file == ''):
        pass
    else:
        grc_dict = make_dict_from_tsv_file(grc_file)
        eng_dict = make_dict_from_tsv_file(eng_file)

        intersection = set(grc_dict.keys()).intersection(set(eng_dict.keys()))
        for key in sorted(intersection):
            # Remove empty keys
            if(len(grc_dict[key]) < 1 or len(eng_dict[key]) < 1):
                intersection.remove(key)
        for key in sorted(intersection):
            greek_save.write(str(grc_dict[key] + '\n'))
            eng_save.write(str(eng_dict[key] + '\n'))
            