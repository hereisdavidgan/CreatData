import csv
import random


def xie(dict1):
    for ii in range(len(dict1)):
        list1 = list(dict1.keys())
        list2 = list(dict1.values())
        aa = list2[ii]
        b = '-->'
        c = list1[ii]
        d = ';\n'
        f.write(aa + b + c + d)


def du(t):
    dept1 = csv.reader(open('..\\csv\\dept.csv', mode='r', encoding='gbk'))
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    print(dept1)
    for iii in dept1:
        list1.append(iii[0])
        list2.append(iii[1])
        list3.append(iii[2])
        list4.append(iii[3])
    for iii in range(int(1.3 * t)):
        list5.append(random.choice(list1)+random.choice(list2)+random.choice(list3))
    temp = {}.fromkeys(list5)
    list7 = list(temp.keys())
    return list7[0:t]


base = [5, 19, 41, ]
target = int(input('要造的部门数：'))
list6 = list(du(target))
print(list6)
jituan = []
yewuqun = []
yewuxian = []
shiyebu = []
jiaofubu = []

for i in range(5):
    a = random.choice(list6)
    jituan.append(a + '集团')
    list6.remove(a)
for i in range(19):
    a = random.choice(list6)
    yewuqun.append(a + '业务群')
    list6.remove(a)
for i in range(41):
    a = random.choice(list6)
    yewuxian.append(a + '业务线')
    list6.remove(a)
for i in range(61):
    a = random.choice(list6)
    shiyebu.append(a + '事业部')
    list6.remove(a)
for i in range(83):
    a = random.choice(list6)
    jiaofubu.append(a + '交付部')
    list6.remove(a)


temp0 = {}
for i in jituan:
    temp0[i] = 'xxx有限公司'    # 添加
temp1 = {}
for i in yewuqun:
    temp1[i] = random.choice(jituan)    # 添加
temp2 = {}
for i in yewuxian:
    temp2[i] = random.choice(yewuqun)    # 添加
temp3 = {}
for i in shiyebu:
    temp3[i] = random.choice(yewuxian)    # 添加
temp4 = {}
for i in jiaofubu:
    temp4[i] = random.choice(shiyebu)    # 添加

print(temp1)

f = open('../csv/1.md', mode='w', encoding='UTF-8')
f.write('```mermaid\n')
f.write('graph LR;\n')
xie(temp0)
xie(temp1)
xie(temp2)
xie(temp3)
xie(temp4)
f.close()

total = []
tlist1 = []
tlist2 = []
for i in jituan:
    total.append(i)
for i in temp1.keys():
    tlist1.append(temp1[i] + '>>' + i)
    total.append(temp1[i] + '>>' + i)
for i in temp2.keys():
    tlist2.append(temp2[i] + '>>' + i)
    total.append(temp2[i] + '>>' + i)
print(total)

