import requests
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
url = 'https://www.olx.ua/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/kiev/'
headers = {
    "User-Agent": generate_user_agent()
}
def links_generator():
    # global url
    generated_url_list = []
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
            generated_url_list.append(generated_url)
        print(generated_url_list)
    return(generated_url_list)
links_generator()

