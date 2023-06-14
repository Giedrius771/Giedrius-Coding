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


def currency_pair_analysis(base_currency, target_currency, start_date, end_date):
    url = f"https://api.frankfurter.app/{start_date}..{end_date}?from={base_currency}&to={target_currency}"
    response = requests.get(url)
    data = response.json()

    rates = data['rates']
    min_rate_date = min(rates.keys())
    max_rate_date = max(rates.keys())

    min_rate = rates[min_rate_date][target_currency]
    max_rate = rates[max_rate_date][target_currency]

    print(f"# Valiutų poroje {base_currency}-{target_currency}, periode nuo {start_date} iki {end_date}:")
    print(f"# Žemiausias kursas buvo {min_rate_date} - {min_rate}")
    print(f"# Aukščiausias kursas buvo {max_rate_date} - {max_rate}")


base_currency = input("Enter the base currency: ")
target_currency = input("Enter the target currency: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

currency_pair_analysis(base_currency, target_currency, start_date, end_date)
