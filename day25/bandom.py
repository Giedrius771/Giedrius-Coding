import requests
from bs4 import BeautifulSoup

url = "https://www.15min.lt/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

blocks = soup.find_all("a", class_="title", attrs={"data-ga-track": "w_Redakcija_rekomenduoja"})

for block in blocks:
    title = block.text.strip()
    if '\n' in title:
        title = title.replace("\n", "")
    print(title)
