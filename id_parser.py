import requests
from bs4 import BeautifulSoup
from time import sleep
import time
from os import system
import json
from user_agent import generate_user_agent
# from selenium import webdriver

url = 'https://www.olx.ua/d/obyavlenie/sdam-na-1-2-mesyatsa-1-k-kvartiru-metro-levobezhnaya-bez-komissii-IDOnMxS.html#5291a2c816'
headers = {
"User-Agent": generate_user_agent()}
# req = requests.get(url, headers = headers).text
def id_extractor(url):
    try:
        # html = open('test.html', 'r')
        req = requests.get(url, headers = headers).text
        soup = BeautifulSoup(req, "lxml")
        id_number = soup.find("span", class_="css-9xy3gn-Text eu5v0x0")
        id_number = id_number.text[4:]
        
        
        print('--------------')
        # print(id_number[-9:-1:1])
        print(id_number)
        
    except(AttributeError):
        # id_extractor(url)
        print('Problem')

if __name__ == "__main__":
    while True:
        # generated_url_list = links_generator()
        # for url in generated_url_list:
        id_extractor(url)
 