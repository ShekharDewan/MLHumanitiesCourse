import sys
import csv
csv.field_size_limit(100000000)

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def make_dict_from_tsv_file(filestring):
	text_for_citation = dict()
	with open(filestring, newline='', encoding = 'UTF-8') as tsv_file:
		#lines= tsv_file.readlines()
		reader = csv.reader(tsv_file, quoting=csv.QUOTE_NONE, delimiter='\t')

		for line in reader:
			try:
			#print(line)
				if(len(line[3]) < 100000):
					text_for_citation[line[0]+line[1]+line[2]] = line[3]
			except Exception as e:
				pass
		#for line in lines:
		#	print(line)
	#print(text_for_citation)
	return text_for_citation


eng_dict = make_dict_from_tsv_file(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\PerseusEnglishOutput.txt')
grek_dict = make_dict_from_tsv_file(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\PerseusGreekInput.txt') #  PerseusGreekInput.txt


for key in list(eng_dict):
	if key not in grek_dict:
		del eng_dict[key]

for key in list(grek_dict):
	if key not in eng_dict:
		del grek_dict[key]

inputGreek = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\inputGreek.txt', 'w', encoding = 'utf-8')
outputEnglish = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\TrainingData\outputEnglish.txt', 'w', encoding = 'utf-8')

for key in grek_dict:
	#if (len(grek_dict[key]) < line_length and len(eng_dict[key]) < line_length):
	greek_verse = str(grek_dict[key])
	eng_verse = str(eng_dict[key])
	# periods_greek = findOccurrences(greek_verse, '.')
	# periods_english = findOccurrences(eng_verse, '.')
	# if (periods_english == periods_greek):
	greek_verse = greek_verse.split('. ')
	eng_verse = eng_verse.split('. ')
	if len(greek_verse) == len(eng_verse):
		for verse in greek_verse:
			inputGreek.write(str(verse + '\n'))
		for verse in eng_verse:
			outputEnglish.write(str(verse + '\n'))

inputGreek.close()
outputEnglish.close()

'''
for item in grek_dict.items():
	print(item[1])
	try:
		print("\t" + eng_dict[item[0]])
	except KeyError:
		print("*** aaargh: greek key ", item[0], "isn't in the English dictionary!")
'''