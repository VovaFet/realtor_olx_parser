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
start_time = time.strftime("%H:%M:%S", time.localtime())
url = 'https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/?page=1'
iteration = 0

def links_generator(url):
    # global url
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, "lxml")
    page_number = soup.find_all("a", class_="block br3 brc8 large tdnone lheight24")
    if page_number==[]:
        generated_url = url
        # print(generated_url)
    else:
        for _ in page_number:
            page = int(_.find("span").text)
        # print(page)
        for gg in range(1,page+1):
            generated_url = url+'?page='+str(gg)
            # print(generated_url)
    return generated_url

def iteration_def(iteration):
    iteration += 1
    return iteration



def main_page(iteration, generated_url):
    # while True:
    count = 0
    all_list = []
    all_ads_title_list = []
    all_ads_price_list = []
    all_ads_links_list = []
    all_ads_time_list = []
    now = time.strftime("%H:%M:%S", time.localtime())
    req = requests.get(generated_url, headers=headers).text
    soup = BeautifulSoup(req, "lxml")
    all_ads_title = soup.find_all("h3", class_="lheight22 margintop5")
    all_ads_links = soup.find_all("a", class_="marginright5 link linkWithHash detailsLink")
    all_ads_links_promoted = soup.find_all("a", class_="marginright5 link linkWithHash detailsLink linkWithHashPromoted")
    all_ads_price = soup.find_all("p", class_="price")
    all_ads_time = soup.find_all("td", class_="bottom-cell")
    all_ads_finded = soup.find("p", class_="color-2")
    print(f"Количество реквестов - {iteration}")
    print(f"Время начала проверки - {start_time}")
    print(f"Время текущего реквеста - {now}")
    # print("Ссылка реквеста -" + generated_url)
    for time_ in all_ads_time:
        time_ = time_.text.strip().replace('Киев,', '').replace('\n\n\n', '')
        all_ads_time_list.append(time_)
    for title in all_ads_title:
        title = title.text.strip()
        all_ads_title_list.append(title)
    for price in all_ads_price:
        price = price.text.strip()
        all_ads_price_list.append(price)
        count += 1
    for links in all_ads_links_promoted:
        links = links.get("href")
        all_ads_links_list.append(links)
    for links in all_ads_links:
        links = links.get("href")
        all_ads_links_list.append(links)
        
    # print(type(all_ads_finded))
    print(all_ads_finded.text)
    print("==================================")
    for i in range(count):
        all_ads_list = [
            f"{i + 1}. {all_ads_time_list[i]} - {all_ads_title_list[i]}: {all_ads_links_list[i]} - {all_ads_price_list[i]}"]
        all_list.append(all_ads_list)
        # sleep(0.25)
        print(all_list[i])
    return start_time, all_list, now


# print(all_list)
def txt_writer(start_time, all_list, now, iteration):
    with open('XATA_FOR_PABLO.txt', 'w') as f:
        f.write(f"\nКоличество реквестов - {iteration}\n")
        f.write(f"Время начала реквестов - {start_time}\n")
        f.write(f'Время текущего реквеста - {now}\n')
        for item in all_list:
            f.write("%s\n" % item)


def csv_writer(start_time, all_list, now, iteration):
    with open('data.csv', 'w') as f:
        f.write(f"\nКоличество реквестов - {iteration}\n")
        f.write(f"Время начала реквестов - {start_time}\n")
        f.write(f"Время текущего реквеста - {now}\n")
        # writer = csv.writer(f)
        for row in all_list:

            f.write("%s\n" % row)
        # writer.writerow(row)
        _ = sleep(5)


if __name__ == "__main__":

    while True:
        iteration = iteration_def(iteration)
        generated_url = links_generator(url)
        start_time, all_list, now = main_page(iteration, generated_url)
        csv_writer(start_time, all_list, now, iteration)
        txt_writer(start_time, all_list, now, iteration)
        _ = system('clear')
        # if iteration == 25:  # choose count of iterarion
            # print('END')
            # break