from bs4 import BeautifulSoup as bs

text = open('Perseus_text.xml')
# text = open('Perseus_text_1999.01.0156.xml')
cleanp = open("Perseus_clean.xml", "w")

soup = bs(text, 'lxml')
soup.prettify()
pn = soup.find_all(["placename","persname","surname"])
for p in pn:
    p.unwrap()


soup
cleanp.write(str(soup))
cleanp.close()