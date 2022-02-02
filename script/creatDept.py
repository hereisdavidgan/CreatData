import csv
import random


def xie1(x2):
    f = open('../csv/resule.csv', mode='w', encoding='UTF-8')
    for x1 in x2:
        for j in x1:
            f.write(j+'\n')


def du(t):
    # 输入要造的部门数，输出备用词条
    dept1 = csv.reader(open('..\\csv\\dept.csv', mode='r', encoding='gbk'))
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    # print(dept1)
    for iii in dept1:
        list1.append(iii[0])
        list2.append(iii[1])
        list3.append(iii[2])
        list4.append(iii[3])
    for iii in range(int(1.3 * t)):
        list5.append(random.choice(list1)+random.choice(list2)+random.choice(list3))
    temp = {}.fromkeys(list5)
    list7 = list(temp.keys())
    return list7


def zhengbei(tt1, tt2):
    # 输入要造的部门数和层级，输出每一层具体要多少个部门
    base1 = [5, 19, 41, 61, 83, 107, 137, 163, 191, 223, 223, 191, 163, 137, 107, 83, 61, 41, 19, 5]
    base2 = []
    t2 = 0
    for t1 in base1[0:tt2]:
        t2 += t1
    t3 = tt1 / t2
    for t4 in base1[0:tt2]:
        base2.append(int(t3 * t4))
    return base2


def shengcheng(s1, s2, s3):
    # 输入s1 那一层要的部门数, s2 备用词条, s3 第几层
    bumen = ["集团", "业务群", "业务线", "事业部", "交付部", "团队", "界", "门", "纲", "目", "科", "属", "种", "甲", "乙", "丙", "丁", "戊", "己",
             "庚", "辛"]
    shengcheng1 = []
    for i1 in range(s1):
        a1 = random.choice(s2)
        shengcheng1.append(a1 + bumen[s3])
        # list6.remove(a1)
    return shengcheng1


def result(r2, r3):
    r1 = [r2[0]]
    for d1 in range(r3 - 1):
        d3 = list(r1[d1])
        r4 = []
        for d2 in r2[d1 + 1]:
            r4.append(random.choice(d3) + '>>' + d2)
        r1.append(r4)
    return r1


target1 = int(input('要造的部门数(约数)：'))
target2 = int(input('要造的层级数(最大20)：'))
result1 = list(zhengbei(target1, target2))
list6 = list(du(target1))
# 生成一个包含各层级的列表
list8 = []
for i in range(target2):
    s = shengcheng(result1[i], list6, i)
    list8.append(s)
result2 = result(list8, target2)
xie1(result2)


