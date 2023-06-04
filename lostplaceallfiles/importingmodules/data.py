# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
import datetime

print(datetime.datetime.now())

print(datetime.date.today())

print(datetime.datetime.now().time())

from datetime import date

print(date.today())

from datetime import date as data

print(data.today())
