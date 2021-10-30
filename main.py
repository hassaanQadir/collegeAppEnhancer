from bs4 import BeautifulSoup

with open('/home/hassaanQadir/.virtualenvs/AlaskaPacificUniversity.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup)
    with open('soupfile.txt', 'w') as file:
        file.write(str(soup))
