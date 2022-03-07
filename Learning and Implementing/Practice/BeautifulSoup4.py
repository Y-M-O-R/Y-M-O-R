from bs4 import BeautifulSoup

with open('Index.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')

tags = doc.find_all('p')
print(tags[0])
print(doc.text)
doc_text = doc.text
d = BeautifulSoup(doc_text, 'html.parser')
print(type(doc_text))
email = d.find_all(text="support@yourcompany.com.")
print(email)
print(type(email))
# may need request to find text
