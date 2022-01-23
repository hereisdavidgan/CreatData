import csv
import random
dept1 = csv.reader(open('..\\csv\\dept.csv', mode='r', encoding='gbk'))
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
print(dept1)
for i in dept1:
    list1.append(i[0])
    list2.append(i[1])
    list3.append(i[2])
    list4.append(i[3])
for i in range(100):
    list5.append(random.choice(list1)+random.choice(list2)+random.choice(list3)+random.choice(list4))

print(list5)
