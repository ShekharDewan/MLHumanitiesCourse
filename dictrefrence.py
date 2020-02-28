import sys
import csv
csv.field_size_limit(100000000)



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
line_length = 500


for key in grek_dict:
	if (len(grek_dict[key]) < line_length and len(eng_dict[key]) < line_length):
		inputGreek.write(str(grek_dict[key] + '\n'))
		outputEnglish.write(str(eng_dict[key] + '\n'))

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