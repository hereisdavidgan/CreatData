import csv
import random

# with open('givenname.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(type(reader))
number = int(input('How Many People You Wannan Creat:'))
givenname1 = csv.reader(open('..\\csv\\givenname.csv', mode='r', encoding='utf-8'))
firstname1 = csv.reader(open('..\\csv\\firstname.csv', mode='r', encoding='utf-8'))
givenname = []
firstname = []

for i in givenname1:
    givenname += i
for i in firstname1:
    firstname += i
lg = len(givenname)
lf = len(firstname)
for i in range(number):
    if i % 10 == 0:
        name = firstname[random.randint(0, lf)]
        name += givenname[random.randint(0, lg)]
    else:
        name = firstname[random.randint(0, lf)]
        name += givenname[random.randint(0, lg)]
        name += givenname[random.randint(0, lg)]
    print(name)