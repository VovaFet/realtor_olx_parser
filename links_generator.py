import requests
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
url = 'https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'
headers = {
    "User-Agent": generate_user_agent()
}
# req = requests.get(url, headers = headers)
# print(req)

# def links_generator():
#     for page_number in range(0,100):
#         req = requests.get(url+'page_number', headers = headers)
#         if req == '<Response [200]>':
#             print(page_number)
def links_generator():
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
            print(generated_url)
        return(generated_url)

links_generator()

