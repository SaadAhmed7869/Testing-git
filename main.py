import os
import requests
import pprint
import urllib3
import urllib
import urllib.request
from libgen_api import LibgenSearch
import json


import pygame # testing version control by addng this

URL = ("https://libgen.li/")
Input = input("Please enter the title of the book you want.\n")


def response_codes():
    search_results = requests.get(URL, verify=False)
    response_code = search_results.status_code

    if response_code != 200:
        print("Error Code : ")
        print(response_code)
    else:
        print("Response code : 200 , Status : A- Okay ")
        filters()
    return search_results


def filters():  # function to get imfo from library genesis
    results1 = LibgenSearch()
    title_filters = {"Extension": "pdf", "Language": "English"}
    titles = results1.search_title_filtered(Input, title_filters, exact_match=True)
    # print(formatted_titles)
    item_to_download = titles[0]
    download_links = results1.resolve_download_links(item_to_download)
    formatted_download_links = json.dumps(download_links, sort_keys=True, indent=4)
    print(formatted_download_links)



print(os.getcwd())
response_codes()


