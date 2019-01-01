import requests
from bs4 import BeautifulSoup
from exception import *


def get_webpage(champion):
    url = 'https://lolprofile.net/champion/' + champion

    page = requests.get(url)

    check_status(page.status_code)

    return page


def get_counter_champions(page):
    # Parses the LoLProfile champion webpage to find the counter champions

    soup = BeautifulSoup(page.text, 'html.parser')

    weak_against = soup.find_all(class_='wa')

    print_n_champions(weak_against, 5) # print top 10 counters

    return weak_against


def print_n_champions(weak_against, n):
    i = 0
    for champion in weak_against:
        if i == n:
            break

        try:
            champion_info = champion.text.split()
            del champion_info[-2:]  # removes the win % and number of games

            champion_name = " ".join(champion_info)

            print(champion_name)
        except ParseException:
            print("Problem parsing the champion name from the weak_against array.")

        i += 1

    return


def check_status(http_code):
    if http_code != 200:
        raise ResponseException("There was a problem reaching LoLProfile. Did you type a valid champion name?")

    return
