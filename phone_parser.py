import requests
id = 743842435
def get_req_url_generator(id):
    req = requests.get(url, headers = headers).text
    soup = BeautifulSoup(req, "lxml")
    id_number = soup.find("span", class_="css-9xy3gn-Text eu5v0x0")
    for _ in id_number:
        id_number = _.text

    headers = {
        'Accept':'*/*',
        'Host': 'www.olx.ua',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode    ': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0', 
        'Authorization': 'Bearer 11490530de11bfea7a772a0e4ecf5f370d8f1d7e'}
    req_get = requests.get(f'https://www.olx.ua/api/v1/offers/{id}/limited-phones/', headers=headers).text.replace('{"data":{"phones":["','')\
        .replace('"]}}','').replace(' ', '').replace('"', '')
    print(req_get)



    
get_req_url_generator(id)