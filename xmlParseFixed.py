import xml.etree.ElementTree as ET

text = open('Perseus_clean.xml', encoding='UTF-8')
# text = open('tlg0527.tlg001.opp-grc2.xml')
# tlg0527.tlg001.opp-grc2.xml

tree = ET.parse(text)
root = tree.getroot()
print(root)

#file = open("testfile.txt", "w")
file = open("genesis.txt", "w", encoding='UTF-8')

file.write("Book" + "\t" + "Chapter" + ":" "Verse" + "\t" + "English Text" + "\n")
# file.write("\n")
for child in root.findall('text'):
    for body in child.findall('div1'):
        for chapter in body.findall('div2'):
            for p in chapter.findall('p'):
                i = 1
                for text in p.itertext():
                    text = text.replace('\t', ' ')
                    text = text.replace('\n', ' ')
                    text = " ".join(text.split())
                    file.write(body.attrib["n"] + "\t" + chapter.attrib["n"] + ":" + str(i) + "\t" + text + "\n")
                    i = i + 1

file.close()