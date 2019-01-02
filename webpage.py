import requests
from bs4 import BeautifulSoup
from exception import *
import json


def get_webpage(champion):
    url = 'https://lolprofile.net/champion/' + champion

    page = requests.get(url)

    check_status(page.status_code)

    return page


def get_counter_champions(page, lane):
    # Parses LoLProfile champion webpage to find the counter champions given the lane you are playing that champion in

    soup = BeautifulSoup(page.text, 'html.parser')

    weak_against = soup.find_all(class_='wa')

    print_n_champions(weak_against, 10, lane)

    return weak_against


def print_n_champions(weak_against, n, lane):
    with open('champion_lanes.json') as f:
        champion_lanes = json.load(f)

    i = 0
    for champion in weak_against:
        if i == n:
            break

        try:
            champion_info = champion.text.split()
            del champion_info[-2:]  # removes the win % and number of games

            champion_name = " ".join(champion_info).lower()
            champion_name = clean_name(champion_name)

            if lane not in champion_lanes[champion_name]:
                continue

            print(champion_name)
        except ParseException:
            print("Problem parsing the champion name from the weak_against array.")

        i += 1

    return


def check_status(http_code):
    if http_code != 200:
        raise ResponseException("There was a problem reaching LoLProfile. Did you type a valid champion name?")

    return


def clean_name(name):
    # TODO: Get rid of this function and use regex to clean strings in one line
    name = name.replace("'", "")

    name = name.replace(".", "")

    if name.startswith("nunu"):
        return "nunu"

    return name
