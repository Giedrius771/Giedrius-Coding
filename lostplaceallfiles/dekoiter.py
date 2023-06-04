# ##### 1 uzduotis ####
# def skaiciuojam_iki(iki):
#     count = 1
#     while count <= iki:
#         if count % 2 != 0:
#             count += 1
#         yield count
#         count += 2
#
# counter = skaiciuojam_iki(10000)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
####### 2 uzduotis
#
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# generatorius = fibonacci_generator()
# fib_sequence = [next(generatorius) for _ in range(28)]
#
# for number in fib_sequence:
#     print(number, end=", ")
## https://www.linkedin.com/pulse/fibonačio-skaičius-auksinė-proporcija-tomas-vytas/?articleId=6626058706666815488 #####
##### 3 uzduotis ####
# def pin_generator(start_pin):
#     pin = start_pin
#     while True:
#         yield pin
#         pin = str(int(pin) + 1).zfill(4)
#         if pin == start_pin:
#             break
#
# correct_pin = '0549'
# generatorius = pin_generator('0000')
#
# for pin in generatorius:
#     print(pin)
#     if pin == correct_pin:
#         print(f"PIN is {correct_pin}")
#         break
#### 4 uzduotis ####
def skaityti_eilutes(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')


file_generator = skaityti_eilutes('atidaromas.txt')

for line in file_generator:
    print(line)
