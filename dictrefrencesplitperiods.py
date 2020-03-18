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
				if(len(line[3]) < max_field_size):
					text_for_citation[line[0]+ '_' + line[1] + '_' + line[2]] = line[3]
			except Exception as e:
				pass
	return text_for_citation


entries = Path(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TitledTrainingData')
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
		#remove really small files. 
        if(len(intersection) < 20):
            pass
        else:
            str_grc = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\MatchedTitledPeriodTrainingData\\' + title + 'GRC.txt'
            str_eng = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\MatchedTitledPeriodTrainingData\\' + title + 'ENG.txt'
            greek_save = open(str_grc, 'w', encoding = 'utf-8')
            eng_save = open(str_eng, 'w', encoding = 'utf-8')
            for key in sorted(intersection):
                grc_split_period = grc_dict[key].split('.')
                eng_split_period = eng_dict[key].split('.')
                if(len(grc_split_period) == len(eng_split_period)):
                    for i in range(len(grc_split_period)):
                        if(len(grc_split_period[i]) > 0):
                            greek_save.write(str(key.split('xml')[-1]) + '\t' + grc_split_period[i] + '.\n')
                            eng_save.write(str(key.split('xml')[-1]) + '\t' + eng_split_period[i] + '.\n')
                    
                elif(len(grc_dict[key]) < no_period_field_size):
                    greek_save.write(str(key.split('xml')[-1]) + '\t' + grc_dict[key] + '\n')
                    eng_save.write(str(key.split('xml')[-1]) + '\t' + eng_dict[key] + '\n')
            greek_save.close()
            eng_save.close()
            if(os.path.getsize(str_grc) < 100 * 1024):
                os.remove(str_grc)
                os.remove(str_eng)
            