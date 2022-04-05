import requests
from bs4 import BeautifulSoup
from time import sleep
import time
# import csv
from os import system
from user_agent import generate_user_agent

headers = {
    "User-Agent": generate_user_agent()
    }
url = 'https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'

req = requests.get(url, headers=headers).text
soup = BeautifulSoup(req, "lxml")

ads_place = soup.find_all("td", class_="bottom-cell")
for place in ads_place:
    # time_ = time_.text.strip().replace('Киев, ', '').replace('\n\n\n', '')
    place = place.find("small", class_="breadcrumb x-normal").text.strip()


ads_time = soup.find_all("div", class_="space rel")

for _ in ads_time:
    time_time = []
    _ = _.text.strip().split("\n")[3]
    time_time.append(_)
    time_ = time_time[::-2]
    time_ = time_[::-1]
    # time_ = ' '.join(map(str, time_))
# print(len(time_))
    
    # time_ = time_[]
    # time_ = time_[0].replace("\n","")
    
    # time_ = time_
    # find_all("small", class_="breadcrumb x-normal")
    # print(time_)
    # print(x)
name = url[-1]
print(name)