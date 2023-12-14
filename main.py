import requests
import os
from bs4 import BeautifulSoup
import datetime as dt

BASE_URL = "https://myaccount.robisonoil.com"
DEBUG_MODE = os.environ["DEBUG_MODE"]

def main(debug_mode):
    """
    grab the data from robison
        log into robison
        get data from dashboard
    catalog data and date
    if the data goes below a certain level, email me
    """
    base_url = get_base_url(debug_mode)
    soup = log_into_website_and_grab_data(base_url)
    current_oil_level = get_oil_level_from_soup(soup)
    print(current_oil_level)


def get_base_url(debug_mode):
    """
    when debugging, we want to go to localhost for webpage requests.
    otherwise, go to the interwebs
    """
    return BASE_URL if debug_mode else "127.0.0.1"


def log_into_website_and_grab_data(base_url):
    # Fill in your details here to be posted to the login form.
    payload = {
        "email_check": os.environ["ROBISON_USERNAME"],
        "password_check": os.environ["ROBISON_PASSWORD"],
        "cmdLogin": "Login"
    }

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        p = s.post(f"{base_url}/login", data=payload)
        page = s.get(f"{base_url}/user-home")
    
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_oil_level_from_soup(soup):
    table_elements = soup.find_all("tbody", class_="pb-0 mb-0")

    str_of_table_items = [x.text.strip() for x in table_elements][0]
    list_of_table_items = str_of_table_items.split(" \n")
    return list_of_table_items[-1]


if __name__ == "__main__":
    main(DEBUG_MODE)
