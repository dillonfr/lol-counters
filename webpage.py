import requests
from bs4 import BeautifulSoup
from exception import ResponseException


def get_webpage(champion):
    url = 'https://lolprofile.net/champion/' + champion

    page = requests.get(url)

    check_status(page.status_code)

    return page


def get_counter_champions(page):
    # Parses the webpage to find the counter champions

    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.find_all(class_='wa'))

    weak_against = soup.find_all(class_='wa')

    i = 0
    for champion in weak_against:
        if i == 10:
            break

        champion_info = champion.text.split()
        del champion_info[-2:]  # removes the win % and number of games

        champion_name = " ".join(champion_info)

        print(champion_name)
        i += 1


def check_status(http_code):
    if http_code != 200:
        raise ResponseException("There was a problem reaching LoLProfile. Did you type a valid champion name?")

    return
