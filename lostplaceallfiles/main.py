a = input ("Įveskite A skaičių:")
b = input ("Įveskite B skaičių:")
if a > b:
    print("Skaičius A didesnis už B")
elif a == b:
    print("Skaičius A yra lygus B")
else:
    print("Skaičius A mažesnis už B")

print("Programos pabaiga")

my_string = "Hello, world!"
print(my_string)

s = 'Monty Python'
print(s[-1])

s = 'Monty Python Naujas'
print(s[-3])

s = 'Monty Python Naujas'
print(s[0:6])

s = 'Monty Python Naujas'
print(s[::-1])

s = 'Monty Python Naujas'
words = s.split()
for word in words:s = 'Monty Python Naujas'

s = 'Monty Python Naujas'
s = s.replace('Python', 'Programming')
print(s)

s = 'Monty Python Naujas'
print(s.upper())

s = 'Monty Python Naujas'
s = s.casefold()
print(s)

print ("Hello iam here")
print ("Today we got a lot stuff to do")
first = 10
second = 15
print(first + second)
first = '100'
second = '150'
print(first + second)

first = 'Test '
second = 3
print(first * second)

print ("Hello my name is Giedrius")
first = 14
second = 24
print(first + second)
first = 'Test'
second = 6
print(first * second)

first = input("Enter first number: ")
second = input("Enter second number: ")
result = int(first) + int(second)
print(result)

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operation = input("Choose an operation (+ or -): ")

if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
else:
    print("Invalid operation selected.")
    exit()

print("Result: ", result)

first = float(input("Iveskite pirma skaiciu: "))
second = float(input("Iveskite antra skaiciu: "))

if first == second:
    print("skaiciai lygus.")
else:
    print("Skaiciai ne lygus.")

number = int(input("Iveskit skaiciu: "))

if number % 3 == 0:
    print("skaicius dalinamas is 3.")
else:
    print("skaicius ne dalinamas is 3.")