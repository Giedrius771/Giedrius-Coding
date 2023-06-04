##### 1 uzduotis #####
import logging
import math

logging.basicConfig(filename='../lostplaceallfiles/informacija.log', level=logging.INFO,
                    format='%(asctime)s, %(levelname)s, %(message)s')


def skaiciuoti_suma(*args):
    result = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {result}")
    return result


def skaiciuoti_suma2(num):
    result = math.sqrt(num)
    logging.info(f"Skaičiaus {num} šaknis: {result}")
    return result


def skaiciuotiilgi(sentence):
    result = len(sentence)
    logging.info(f"Sakinio '{sentence}' simboliu kiekis: {result}")
    return result


def dalyba(x, y):
    result = x / y
    logging.info(f"Rezultatas, padalinus {x} iš {y}: {result}")
    return result


result_sum = skaiciuoti_suma(20, 30, 40, 60)
print(result_sum)

result_sqrt = skaiciuoti_suma2(25)
print(result_sqrt)

result_count = skaiciuotiilgi("Siandien jau antradienis kai gerai")
print(result_count)

result_division = dalyba(125, 5)
print(result_division)
##### 2 uzduotis #####
import logging
import math

logging.basicConfig(filename='../lostplaceallfiles/inform.log', level=logging.INFO,
                    format='%(asctime)s, %(levelname)s, %(message)s')


def skaiciuoti_suma(*args):
    result = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {result}")
    return result


def skaiciuoti_suma2(num):
    try:
        result = math.sqrt(num)
        logging.info(f"Skaičiaus {num} šaknis: {result}")
        return result
    except Exception as e:
        logging.exception(f"Išimtis įvyko skaičiuojant šaknį: {e}")


def skaiciuotiilgi(sentence):
    result = len(sentence)
    logging.info(f"Sakinio '{sentence}' simboliu kiekis: {result}")
    return result


def dalyba(x, y):
    try:
        result = x / y
        logging.info(f"Rezultatas, padalinus {x} iš {y}: {result}")
        return result
    except ZeroDivisionError as e:
        logging.exception(f"Išimtis įvyko dalyboje iš nulio: {e}")


result_sum = skaiciuoti_suma(10, 20, 30, 40)
print(result_sum)

result_sqrt = skaiciuoti_suma2(25)
print(result_sqrt)

result_count = skaiciuotiilgi("Kaip silta lauke varom i lauka!")
print(result_count)

result_division = dalyba(100, 4)
print(result_division)

result_sqrt_str = skaiciuoti_suma2("test")
print(result_sqrt_str)

result_division_zero = dalyba(10, 0)
print(result_division_zero)
### 3 uzduotis ####
import logging
import math

logger = logging.getLogger('custom_logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('../lostplaceallfiles/inform.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def skaiciuoti_suma(*args):
    result = sum(args)
    logger.info(f"Skaiciu {args} suma lygi: {result}")
    return result


def skaiciuoti_suma2(num):
    try:
        result = math.sqrt(num)
        logger.info(f"Skaičiaus {num} šaknis: {result}")
        return result
    except Exception as e:
        logger.exception(f"Išimtis įvyko skaičiuojant šaknį: {e}")


def skaiciuotiilgi(sentence):
    result = len(sentence)
    logger.info(f"Sakinio '{sentence}' simboliu kiekis: {result}")
    return result


def dalyba(x, y):
    try:
        result = x / y
        logger.info(f"Rezultatas, padalinus {x} iš {y}: {result}")
        return result
    except ZeroDivisionError as e:
        logger.exception(f"Išimtis įvyko dalyboje iš nulio: {e}")


result_sum = skaiciuoti_suma(10, 20, 30, 40)
print(result_sum)

result_sqrt = skaiciuoti_suma2(25)
print(result_sqrt)

result_count = skaiciuotiilgi("Kaip silta lauke varom i lauka!")
print(result_count)

result_division = dalyba(100, 4)
print(result_division)

result_sqrt_str = skaiciuoti_suma2("test")
print(result_sqrt_str)

result_division_zero = dalyba(10, 0)
print(result_division_zero)