import requests
import os
from bs4 import BeautifulSoup
import datetime as dt

def main():
    """
    grab the data from robison
        log into robison
        get data from dashboard
    catalog data and date
    if the data goes below a certain level, email me
    """
    soup = log_into_website_and_grab_data()
    current_oil_level = get_oil_level_from_soup(soup)


def log_into_website_and_grab_data():
    # Fill in your details here to be posted to the login form.
    payload = {
        "email_check": os.environ["ROBISON_USERNAME"],
        "password_check": os.environ["ROBISON_PASSWORD"],
        "cmdLogin": "Login"
    }

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        p = s.post('https://myaccount.robisonoil.com/login', data=payload)
        page = s.get('https://myaccount.robisonoil.com/user-home')
    
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_oil_level_from_soup(soup):
    table_elements = soup.find_all("tbody", class_="pb-0 mb-0")

    str_of_table_items = [x.text.strip() for x in table_elements][0]
    list_of_table_items = str_of_table_items.split(" \n")
    return list_of_table_items[-1]


if __name__ == "__main__":
    main()
