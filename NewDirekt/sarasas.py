# command / ir uzkomentuos eilutes arba kopijuota teksta ###
######## map ir lambda funkcijos trumpai #######
items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product4", 14),
    ("Product5", 18),
    ("Product6", 21),
    ("Product7", 83),
]


prices = list(map(lambda item: item[1], items))
print(prices)


filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
############## List Comprehensions ###################
my_list = [1, 2 ,3, 4, 5, 6, 7]
double = [item *2 for item in my_list]
for item in my_list:
    double.append(item * 2)
print(double)
###########################
users = [{'name': 'Giedrius', 'age': 32}, {'name': 'Tomukas', 'age': 23}, {'name': 'Darius', 'age': 65}]
user_name = [user['name'] for user in users if user['age'] > 30 and user['name'] == 'Darius'] ## rodo tik ta varda kuris iki 30 metu
print(user_name)

user_groups = [
    [
        {'name': 'Marius', 'age': 31},
        {'name': 'Giedrius', 'age': 30}
    ],
    [
        {'name': 'Sarah', 'age': 29},
        {'name': 'Julie', 'age': 45}
    ]
]

user_name = [person['name'] for group in user_groups for person in group if person['age'] > 30]
print(user_name)
###Mean , Median and Mode
def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    return total / len(list_of_nums)

def mode(list_of_nums):
    max_count = (0, 0)
    for number in list_of_nums:
        occurences = list_of_nums.count(number)
        if occurences > max_count[0]:
            max_count = (occurences, number)
    return max_count[1]

def median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 !=0:
        middle_index = int((len(list_of_nums) - 1) / 2) #17
        return list_of_nums[middle_index]
    elif len(list_of_nums) % 2 == 0:
        middle_index_1 = int(len(list_of_nums) / 2)
        middle_index_2 = int(len(list_of_nums) / 2) - 1
        return mean([list_of_nums[middle_index_1], list_of_nums[middle_index_2]])

print(mean([13,13,13,13,14,14,16,18])) #Ats 14.25
print(median([13,13,13,13,14,14,16,18])) #Ats 13.5
print(mode([13,13,13,13,14,14,16,18])) #Ats 13
## LEAP YEARS LENGVIAU
import calendar

metai = list(range(1900, 2150))
leap_years = filter(calendar.isleap, metai)
print(list(leap_years))