###### 1 uzduotis #####
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.15min.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokas = soup.find('div', class_='widget-horizontal-items swipeable')
rekomendacija = blokas.find('h3').text
listas = blokas.find_all('div', class_='item type_1')
print(f'{rekomendacija}:')
for x in listas:
    antraste = x.find('a', class_='title').text.strip()
    print(f'Antraste:\n{antraste}')
    print('----------------------------------------------------------------------------------------------')
###### 2 Uzduotis ####
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
block = soup.find_all('a', class_='CBarticleTitle')
sum = 0
for element in block:
    sum += 1
print(sum)
##### 3 uzduotis ####
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_='mobiles-product-card card card__product card--anim js-product-compare-product')
pigiausias_modelis = None
brangiausias_modelis = None
pigiausia_kaina = float('inf')
brangiausia_kaina = float('-inf')
for blokas in blokai:
    try:
        pavadinimas = blokas.find('a', class_='mobiles-product-card__title js-open-product').text.strip()
        kaina = blokas.find_all('div', class_='mobiles-product-card__price-marker')[1].text.strip()
        kaina = float(kaina.replace(' ', '').replace('€', ''))
        if kaina < pigiausia_kaina:
            pigiausia_kaina = kaina
            pigiausias_modelis = pavadinimas
        if kaina > brangiausia_kaina:
            brangiausia_kaina = kaina
            brangiausias_modelis = pavadinimas
    except:
        pass
print(f'Pigiausias modelis: {pigiausias_modelis} ({pigiausia_kaina} €)')
print(f'Brangiausias modelis: {brangiausias_modelis} ({brangiausia_kaina} €)')
