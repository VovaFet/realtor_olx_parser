import requests
from bs4 import BeautifulSoup
from time import sleep
import time
from os import system
import json
from user_agent import generate_user_agent

# headers = {
#     "User-Agent": generate_user_agent()
#     }
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.olx.ua',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
start_time = time.strftime("%H:%M:%S", time.localtime())
url = 'https://www.olx.ua/nedvizhimost/kvartiry/kiev/'


# iteration = 0
# count = 0

# def iteration_def(iteration):
#     iteration += 1
#     return iteration

def links_generator(url):
    list_of_generated_urls = []
    # global url
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, "lxml")
    page_number = soup.find_all("a", class_="block br3 brc8 large tdnone lheight24")
    if page_number == []:
        print("Менее одной страницы объявлений")
        generated_url = url
        gg = 1
        list_of_generated_urls.append([generated_url, gg])
        return list_of_generated_urls

    else:
        for _ in page_number:
            page = int(_.find("span").text)
        for gg in range(1, page + 1):
            generated_url = url + '?page=' + str(gg)
            list_of_generated_urls.append([generated_url, gg])
    return list_of_generated_urls


def url_parser(generated_url):
    count = 0
    all_all = []
    # ads_time_list = []
    ads_title_list = []
    ads_price_list = []
    ads_link_list = []
    ads_place_list = []
    time_time = []

    # now = time.strftime("%H:%M:%S", time.localtime())
    req = requests.get(generated_url, headers=headers).text
    soup = BeautifulSoup(req, "lxml")
    ads_title = soup.find_all("h3", class_="lheight22 margintop5")
    ads_links_nonprom = soup.find_all("a", class_="marginright5 link linkWithHash detailsLink")
    ads_links_promoted = soup.find_all("a", class_="marginright5 link linkWithHash detailsLink linkWithHashPromoted")
    ads_link = ads_links_promoted + ads_links_nonprom
    ads_price = soup.find_all("p", class_="price")
    ads_place = soup.find_all("td", class_="bottom-cell")
    ads_time = soup.find_all("div", class_="space rel")
    # ads_finded = soup.find("p", class_="color-2")

    for place in ads_place:
        place = place.find("small", class_="breadcrumb x-normal").text.strip()
        ads_place_list.append(place)

    for _ in ads_time:
        _ = _.text.strip().split("\n")[3]
        time_time.append(_)
        time_ = time_time[::-2]
        time_ = time_[::-1]

    for title in ads_title:
        title = title.text.strip()
        ads_title_list.append(title)

    for price in ads_price:
        price = price.text.strip()
        ads_price_list.append(price)
        count += 1

    for links in ads_link:
        links = links.get("href")
        ads_link_list.append(links)

        # print(ads_link_list)

    def id_extractor():
        ads_id_number_list = []
        nonlocal ads_link_list

        for url in ads_link_list:
            try:
                req = requests.get(url, headers=headers).text
                soup = BeautifulSoup(req, features="lxml")
                id_number = soup.find("span", class_="css-9xy3gn-Text eu5v0x0")
                id_number = id_number.text[4:]
                ads_id_number_list.append(id_number)
            except(AttributeError):
                # id_extractor()
                ads_id_number_list.append('Не найдено')
        return ads_id_number_list
        # print(ads_id_number_list)
        # return ads_id_number_list

    ads_id_number_list = id_extractor()
    print(ads_id_number_list)
    def phone_parser():
        ads_phone_number_list = []
        nonlocal ads_id_number_list
        headers = {
            'Accept': '*/*',
            'Host': 'www.olx.ua',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode    ': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Authorization': 'Bearer 389b64bf21419ed2bcd1961e656b15fac22a37eb'}
        for ads_id_number in ads_id_number_list:
                phone_number = requests.get(f'https://www.olx.ua/api/v1/offers/{ads_id_number}/limited-phones/',
                                            headers=headers).text.replace('{"data":{"phones":["', '').replace(
                    '"]}}', '').replace(' ', '').replace('"', '')
                ads_phone_number_list.append(phone_number)
        return ads_phone_number_list

    ads_phone_number_list = phone_parser()

    for i in range(count):
        all_all.append({
            "Дата публикации": time_[i],
            "Место": ads_place_list[i],
            "Цена": ads_price_list[i],
            "Название объявления": ads_title_list[i],
            "Ссылка": ads_link_list[i],
            "ID": ads_id_number_list[i],
            "Номер телефона": ads_phone_number_list[i]
        })
        # print(all_all)
    return all_all


def json_writer(all_all, gg):
    with open(f"data/{gg}_page.json", "w", encoding="utf-8") as file:
        json.dump(all_all, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    while True:
        iteration = 0
        list_of_generated_urls = links_generator(url)
        for (generated_url, gg) in list_of_generated_urls[0:1]:
            all_all = url_parser(generated_url)
            json_writer(all_all, gg)
            iteration += 1
            if iteration == len(list_of_generated_urls):
                _ = system('clear')
                print("PARSING ENDED")
        break