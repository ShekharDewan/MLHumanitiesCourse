import random

'''
Splits data from a folder containing txt files into dev, train and test text files. Ideal for ML. 
'''
inputGreek = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\InputGreek.txt'
outputEnglish = r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\OutputEnglish.txt'
greekLines = open(inputGreek, 'r', encoding = 'utf-8').readlines()
englishLines = open(outputEnglish, 'r', encoding = 'utf-8').readlines()


num_linesGrc = len(greekLines)
num_linesEng = len(englishLines)

if (num_linesEng != num_linesGrc):
    print("Help! The line numbers don't match")
    exit()

lines = list(range(0, num_linesGrc))
random.shuffle(lines)
shuffled_lines = lines
num_lines = num_linesGrc

train_size = int(num_lines * 0.9)
dev_size = int(num_lines * .95)
test_size = int(num_lines)

train_source = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\train_source.txt', 'w', encoding = 'utf-8')
train_target = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\train_target.txt', 'w', encoding = 'utf-8')
dev_source = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\dev_source.txt', 'w', encoding = 'utf-8')
dev_target = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\dev_target.txt', 'w', encoding = 'utf-8')
test_source = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\test_source.txt', 'w', encoding = 'utf-8')
test_target = open(r'C:\Users\shekh\Google Drive\Courses At Mount Allison_\Winter 2020\MLHumanitiesCourse\SockeyeReady\test_target.txt', 'w', encoding = 'utf-8')

i = 0
while (i < num_lines):
    line_number = shuffled_lines[i]
    greekLine = greekLines[line_number]
    englishLine = englishLines[line_number]
    
    if (i < train_size):
        train_source.write(greekLine)
        train_target.write(englishLine)
    elif (i < dev_size):
        dev_source.write(greekLine)
        dev_target.write(englishLine)
    else:
        test_source.write(greekLine)
        test_target.write(englishLine)
    i += 1


#os.remove(inputGreek)
#os.remove(outputEnglish)
# englishLines.close()
train_source.close()
train_target.close()
dev_source.close()
dev_target.close()
test_source.close()
test_target.close()