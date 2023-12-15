import requests
import os
from bs4 import BeautifulSoup
import datetime as dt
import csv
import time
import logging
import logging.config

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger(__name__)

BASE_URL = "https://myaccount.robisonoil.com"
DEBUG_MODE = os.getenv("DEBUG_MODE")
ROBISON_USERNAME = os.getenv("ROBISON_USERNAME")
ROBISON_PASSWORD = os.getenv("ROBISON_PASSWORD")
THRESHOLD = 100

def main(debug_mode):
    """
    grab the data from robison
        log into robison
        get data from dashboard
    catalog data and date
    if the data goes below a certain level, email me
    """
    # while True:
    base_url = get_base_url(debug_mode)
    soup = log_into_website_and_grab_data(base_url, ROBISON_USERNAME, ROBISON_PASSWORD)
    oil_level = get_oil_level_from_soup(soup)
    maybe_alert_user(oil_level, THRESHOLD)
    
    datapoint = {
        "date": dt.datetime.now(), 
        "oil_level": oil_level
    }

    add_oil_level_to_csv(datapoint)
        # time.sleep(86400) # sleep for 1 day


def get_base_url(debug_mode):
    """
    when debugging, we want to go to localhost for webpage requests.
    otherwise, go to the interwebs
    """
    return "http://127.0.0.1:5000" if debug_mode else BASE_URL


def log_into_website_and_grab_data(base_url, username, password):
    # Fill in your details here to be posted to the login form.
    payload = {
        "email_check": username,
        "password_check": password,
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


def add_oil_level_to_csv(datapoint):
    with open("oil_levels.csv", "a") as csvfile:
        fieldnames = ["date", "oil_level"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(datapoint)


def maybe_alert_user(oil_level, threshold):
    if float(oil_level) <= threshold:
        logger.warning(f"Oil Level is at {oil_level}")


if __name__ == "__main__":
    main(DEBUG_MODE)
