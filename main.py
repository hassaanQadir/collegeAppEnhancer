from bs4 import BeautifulSoup
import requests

numbers = [1,2,3]

for n in numbers:
    targetURL = ("https://apply.commonapp.org/mycolleges/443/2303/627%s" % n)

    #here we put that file into a variable. We also print the name onto the command line to make sure the program is running
    applicationPage = requests.get(targetURL, stream = True)

    with open("target.html", mode='wb') as targetHTML:
        targetHTML.write(applicationPage.content)

    with open("target.html") as targetHTML:
        soup = BeautifulSoup(targetHTML, 'html.parser')
        print(soup.title.text)
        for label in soup.select('li.zone label'):
            print(label.string)
        with open('soupfile.txt', 'a') as file:
            file.write(str(soup.prettify))

