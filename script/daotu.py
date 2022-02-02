import csv
import random


dept0 = list(csv.reader(open('..\\csv\\result.csv', mode='r', encoding='utf-8')))
dept1 = []
for i in dept0:
    dept1.append(i[0])
print(dept1)
dept1.reverse()
temp1 = [dept1[0]]

# dept1 = ['1', '2', '3', '4', '5', '3', '33']
# dept1.reverse()
# temp1 = [dept1[0]]
for i in dept1:
    active = True
    for j in temp1:
        if i in j:
            active = False
    if active:
        temp1.append(i)
print(temp1)
