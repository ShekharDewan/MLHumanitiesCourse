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

eng_dict = make_dict_from_tsv_file(sys.argv[1])
grek_dict = make_dict_from_tsv_file(sys.argv[2])

# trainingInput = open('input.txt', 'w', encoding = 'UTF-8')
# trainingOutput = open('input.txt', 'w', encoding = 'UTF-8')

for item in grek_dict.items():

	print(item[1])
	try:
		print("\t" + eng_dict[item[0]])
	except KeyError:
		print("*** aaargh: greek key ", item[0])

for item in eng_dict.items():
	try:
		print(grek_dict[item[0]])
	except KeyError:
		print("*** aaargh: engli key ", item[0])
