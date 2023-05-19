#1 uzduotis
# -1 dalis
def refine_sum(num1, num2, num3):
    return round(num1 + num2 + num3, 2)

result = refine_sum(3, 2, 1)
print(result)

## 2-dalis
def refund_amount(num_list):
    return sum(num_list)

result = refund_amount([10, 20, 30])
print(result)
## 3-dalis
def print_largest_number(*args):
    return max(args)

result = print_largest_number(10, 20, 30, 40)
print(result)
## 4-dalis
def beautify_backwards(s):
    return s[::-1]

result = beautify_backwards("Siandien yra ketvirtadienis!")
print(result)
### 5-dalis
def count_chars(s):
    num_words = len(s.split())
    num_upper = sum(1 for c in s if c.isupper())
    num_lower = sum(1 for c in s if c.islower())
    return num_words, num_upper, num_lower

result = count_chars("Labas jau ritoj BUS penktadienis, kaip gerai, VALIO!!")
print(result)
## 6 - dalis
def unique_list(num_list):
    return list(set(num_list))

result = unique_list([1, 2, 3, 2, 4, 3, 5, 1, 2, 3, 5])
print(result)
## 7 - dalis
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

result = is_prime(47)
print(result)
## 8 - dalis
def line_up_words(s):
    words = s.split()
    return ' '.join(reversed(words))

result = line_up_words("As labai laukiu savaitgalio")
print(result)
### 9 - dalis
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
result = is_leap_year(2024)
print(result)
## 10 - dalis
import datetime

def time_since_anniversary():
    anniversary = input("Iveskite sukaktuviu data in 'YYYY-MM-DD HH:MM:SS' formatas: ")
    now = datetime.datetime.now()
    anniversary = datetime.datetime.strptime(anniversary, '%Y-%m-%d %H:%M:%S')
    time_passed = now - anniversary
    years = time_passed.days // 365
    months = time_passed.days % 365 // 30
    days = time_passed.days % 365 % 30
    hours = time_passed.seconds // 3600
    minutes = time_passed.seconds % 3600 // 60
    seconds = time_passed.seconds % 3600 % 60
    return f'{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

print(time_since_anniversary())

# 2 Uzduotis - 1dalis
def is_half_equal(num):
    num_str = str(num)
    mid = len(num_str) // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    return first_half == second_half

print(is_half_equal(1212))
print(is_half_equal(1234))
# 2/ 2dalis
def contiguous_number(num):
    num_str = str(num)
    output = ""
    for i in range(len(num_str) - 1):
        output += f"{num_str[i]} - {num_str[i]}{num_str[i + 1]}, "
    output += f"{num_str[-1]} - {int(num_str[-1]) + 1}"
    return output


print(contiguous_number(3798))
## 3 uzduotis
def is_valid_personal_code(personal_code):
    if not personal_code.isdigit() or len(personal_code) != 11:
        return False

    gender = int(personal_code[6])
    if gender not in [1, 2, 3, 4, 5, 6, 7, 8]:
        return False

    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    digits = list(map(int, personal_code))
    total = sum([f * d for f, d in zip(factors, digits)]) % 11 % 10
    return total == digits[-1]

personal_code = input("Iveskite asmens koda: ")
print(is_valid_personal_code(personal_code))
## 3 /2 dalis ##
import datetime

def is_valid_personal_code(personal_code):
    if not personal_code.isdigit() or len(personal_code) != 11:
        return False

    gender = int(personal_code[6])
    if gender not in [1, 2, 3, 4, 5, 6, 7, 8]:
        return False

    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    digits = list(map(int, personal_code))
    total = sum([f * d for f, d in zip(factors, digits)]) % 11 % 10
    return total == digits[-1]


def generate_personal_code(date_of_birth, gender, serial_number):
    year_last_digits = str(date_of_birth.year)[-2:]
    month = str(date_of_birth.month)
    day = str(date_of_birth.day)
    gender_digit = str(gender)
    serial_number_digits = str(serial_number).zfill(3)
    personal_code = year_last_digits + month.zfill(2) + day.zfill(2) + gender_digit + serial_number_digits

    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    digits = list(map(int, personal_code))
    total = sum([f * d for f, d in zip(factors, digits)]) % 11 % 10
    last_digit = total if total < 10 else 0

    return personal_code + str(last_digit)


# Pavizdys naudojimo
date_of_birth = datetime.date(1990, 1, 1)
gender = 3
serial_number = 123
personal_code = generate_personal_code(date_of_birth, gender, serial_number)
print(personal_code)
print(is_valid_personal_code(personal_code))

sadas
######
