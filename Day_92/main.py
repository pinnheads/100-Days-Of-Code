import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Request Line": "GET / HTTP/1.1",
}

response = requests.get("https://steamdb.info/graph/", headers=headers)
data = response.text
print(response.status_code)

soup = BeautifulSoup(data, "html.parser")
rows = soup.find_all("tr", {"class": "app"})

tds = []
for row in rows:
    tds.append(row.findAll("td")[3::])


with open("steam_game_data.csv", "a+") as data_file:
    data_file.write("index,name,current_players,24_peak,all_time_peak\n")
    for td in tds:
        print(
            td[0].find("a").text,
            (td[1].text).replace(",", ""),
            (td[2].text).replace(",", ""),
            (td[3].text).replace(",", ""),
        )
        data_file.write(
            f"{td[0].find('a').text},{(td[1].text).replace(',', '')},{(td[2].text).replace(',', '')},{(td[3].text).replace(',', '')}\n"
        )
