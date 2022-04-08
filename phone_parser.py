import requests
from bs4 import BeautifulSoup
from time import sleep
import time
from os import system
import json
from user_agent import generate_user_agent
# url = "https://www.olx.ua/d/obyavlenie/prodam-vaz-2101-v-horoshem-sostoyanii-IDOdSMK.html#2eb1d769fe"


id =  742125662
def phone_parser():
    ads_phone_number_list = []
    headers = {
        'Accept':'*/*',
        'Host': 'www.olx.ua',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode    ': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0', 
        'Authorization': 'Bearer 925d4e92c6454e6fd4e6e2c1414af7b5befcf309'}

    req_get = requests.get(f'https://www.olx.ua/api/v1/offers/{id}/limited-phones/', headers=headers).text.replace('{"data":{"phones":["','')\
        .replace('"]}}','').replace(' ', '').replace('"', '')

