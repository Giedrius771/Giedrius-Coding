# ######### 1 uzduotis ####
# import requests
#
# def get_rate(base_currency, target_currency):
#     url = f"https://api.frankfurter.app/latest?base={base_currency}"
#     response = requests.get(url)
#     data = response.json()
#
#     if 'rates' in data:
#         rates = data['rates']
#         if target_currency in rates:
#             rate = rates[target_currency]
#             currency_name = get_currency_name(target_currency)
#             print(f"{base_currency} to {target_currency} ({currency_name}): {rate}")
#         else:
#             print(f"{base_currency} to {target_currency}: Invalid currency pair.")
#     else:
#         print("Unable to fetch exchange rates.")
#
# def get_currency_name(currency_code):
#     currency_names = {
#         'AUD': 'Australian Dollar',
#         'BGN': 'Bulgarian Lev',
#         'BRL': 'Brazilian Real',
#         'CAD': 'Canadian Dollar',
#         'CHF': 'Swiss Franc',
#         'CNY': 'Chinese Yuan',
#         'CZK': 'Czech Koruna',
#         'DKK': 'Danish Krone',
#         'EUR': 'Euro',
#         'GBP': 'British Pound',
#         'HKD': 'Hong Kong Dollar',
#         'HUF': 'Hungarian Forint',
#         'IDR': 'Indonesian Rupiah',
#         'ILS': 'Israeli New Shekel',
#         'INR': 'Indian Rupee',
#         'ISK': 'Icelandic Króna',
#         'JPY': 'Japanese Yen',
#         'KRW': 'South Korean Won',
#         'MXN': 'Mexican Peso',
#         'MYR': 'Malaysian Ringgit',
#         'NOK': 'Norwegian Krone',
#         'NZD': 'New Zealand Dollar',
#         'PHP': 'Philippine Peso',
#         'PLN': 'Polish Złoty',
#         'RON': 'Romanian Leu',
#         'RUB': 'Russian Ruble',
#         'SEK': 'Swedish Krona',
#         'SGD': 'Singapore Dollar',
#         'THB': 'Thai Baht',
#         'TRY': 'Turkish Lira',
#         'USD': 'US Dollar',
#         'ZAR': 'South African Rand',
#     }
#     return currency_names.get(currency_code, '')
#
# all_currencies = [
#     'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
#     'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR',
#     'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR'
# ]
#
# print("List of available currencies:")
# for currency in all_currencies:
#     currency_name = get_currency_name(currency)
#     print(f"{currency} - {currency_name}")
#
# base_currency = input("Enter the base currency: ")
# target_currency = input("Enter the target currency: ")
#
# if base_currency not in all_currencies:
#     print("Invalid base currency.")
# else:
#     get_rate(base_currency, target_currency)
# ###### 2 uzduotis ####
# # import requests
# # from bs4 import BeautifulSoup
# # from datetime import datetime
# #
# #
# # def get_horoscope_from_website(zodiac_sign):
# #     url = (
# #         "https://www.horoscope.com/us/horoscopes/general/"
# #         f"horoscope-general-daily-today.aspx?sign={zodiac_sign}"
# #     )
# #     soup = BeautifulSoup(requests.get(url).content, "html.parser")
# #     return soup.find("div", class_="main-horoscope").p.text
# #
# #
# # def get_horoscope_from_api(zodiac_sign):
# #     url = "https://horoscopeapi-horoscope-v1.p.rapidapi.com/daily"
# #     querystring = {"date": datetime.today().strftime("%Y-%m-%d")}
# #     headers = {
# #         "X-RapidAPI-Key": "YOUR_API_KEY",
# #         "X-RapidAPI-Host": "horoscopeapi-horoscope-v1.p.rapidapi.com"
# #     }
# #     response = requests.get(url, headers=headers, params=querystring)
# #     return response.json()["horoscope"]
# #
# #
# # if __name__ == "__main__":
# #     dic = {'Aries': 1, 'Taurus': 2, 'Gemini': 3,
# #            'Cancer': 4, 'Leo': 5, 'Virgo': 6,
# #            'Libra': 7, 'Scorpio': 8, 'Sagittarius': 9,
# #            'Capricorn': 10, 'Aquarius': 11, 'Pisces': 12}
# #
# #     print('Choose your zodiac sign from the list below:')
# #     print('[Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra,'
# #           ' Scorpio, Sagittarius, Capricorn, Aquarius, Pisces]')
# #
# #     zodiac_sign = dic[input("Input your zodiac sign: ")]
# #     horoscope_text = get_horoscope_from_website(zodiac_sign)
# #     print(horoscope_text)
#
# #### 2 uzduotis pakeita ######
# import requests
#
#
# def currency_pair_analysis(base_currency, target_currency, start_date, end_date):
#     url = f"https://api.frankfurter.app/{start_date}..{end_date}?from={base_currency}&to={target_currency}"
#     response = requests.get(url)
#     data = response.json()
#
#     rates = data['rates']
#     min_rate_date = min(rates.keys())
#     max_rate_date = max(rates.keys())
#
#     min_rate = rates[min_rate_date][target_currency]
#     max_rate = rates[max_rate_date][target_currency]
#
#     print(f"# Valiutų poroje {base_currency}-{target_currency}, periode nuo {start_date} iki {end_date}:")
#     print(f"# Žemiausias kursas buvo {min_rate_date} - {min_rate}")
#     print(f"# Aukščiausias kursas buvo {max_rate_date} - {max_rate}")
#
#
# base_currency = input("Enter the base currency: ")
# target_currency = input("Enter the target currency: ")
# start_date = input("Enter the start date (YYYY-MM-DD): ")
# end_date = input("Enter the end date (YYYY-MM-DD): ")
#
# currency_pair_analysis(base_currency, target_currency, start_date, end_date)
import requests


def get_rate(base_currency, target_currency):
    url = f"https://api.frankfurter.app/latest?base={base_currency}"
    response = requests.get(url)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']
        if target_currency in rates:
            rate = rates[target_currency]
            currency_name = get_currency_name(target_currency)
            print(f"{base_currency} to {target_currency} ({currency_name}): {rate}")
        else:
            print(f"{base_currency} to {target_currency}: Invalid currency pair.")
    else:
        print("Unable to fetch exchange rates.")


def get_currency_name(currency_code):
    currency_names = {
        'AUD': 'Australian Dollar',
        'BGN': 'Bulgarian Lev',
        'BRL': 'Brazilian Real',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan',
        'CZK': 'Czech Koruna',
        'DKK': 'Danish Krone',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'HKD': 'Hong Kong Dollar',
        'HUF': 'Hungarian Forint',
        'IDR': 'Indonesian Rupiah',
        'ILS': 'Israeli New Shekel',
        'INR': 'Indian Rupee',
        'ISK': 'Icelandic Króna',
        'JPY': 'Japanese Yen',
        'KRW': 'South Korean Won',
        'MXN': 'Mexican Peso',
        'MYR': 'Malaysian Ringgit',
        'NOK': 'Norwegian Krone',
        'NZD': 'New Zealand Dollar',
        'PHP': 'Philippine Peso',
        'PLN': 'Polish Złoty',
        'RON': 'Romanian Leu',
        'RUB': 'Russian Ruble',
        'SEK': 'Swedish Krona',
        'SGD': 'Singapore Dollar',
        'THB': 'Thai Baht',
        'TRY': 'Turkish Lira',
        'USD': 'US Dollar',
        'ZAR': 'South African Rand',
    }
    return currency_names.get(currency_code, '')


all_currencies = [
    'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
    'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR',
    'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR'
]

print("List of available currencies:")
for currency in all_currencies:
    currency_name = get_currency_name(currency)
    print(f"{currency} - {currency_name}")

base_currency = input("Enter the base currency: ")
target_currency = input("Enter the target currency: ")

if base_currency not in all_currencies:
    print("Invalid base currency.")
else:
    get_rate(base_currency, target_currency)
