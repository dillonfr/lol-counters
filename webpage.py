import requests
from bs4 import BeautifulSoup

url = 'https://lolprofile.net/champion/'

#TODO: Write JSON file with champion names and their lanes
#TODO: Refactoring
#TODO: Write some tests (test reading from json, test refactored function
#TODO: Find closest champion name to string input using difflib

try:
    champion = str(input("Enter champion name: "))
    url += champion
    print(url)

    page = requests.get(url)

    print(page.status_code) # TODO: check code is 200
    print("done")

    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.find_all(class_='wa'))

    weakAgainst = soup.find_all(class_='wa')

    i = 0
    for champion in weakAgainst:
        if i == 10:
            break
        # print(tag.find('a', href=True)['href'])
        championInfo = champion.text.split()
        del championInfo[-2:]  # remove the win % and number of games

        championName = " ".join(championInfo)

        print(championName)
        i += 1
except:
    "Invalid name?" # TODO: cant reach this code with an invalid name, fix


# url = 'https://lolprofile.net/champion/Alistar'





#print(soup.prettify())
