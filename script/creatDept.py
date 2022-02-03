import csv
import random


def xie1(x2):
    f = open('../csv/result.csv', mode='w', encoding='UTF-8')
    for x1 in x2:
        for j in x1:
            f.write(j+'\n')


def du(t):
    # 输入要造的部门数，输出备用词条
    dept1 = csv.reader(open('..\\csv\\dept.csv', mode='r', encoding='gbk'))
    list1 = []
    list2 = []
    list3 = []
    list5 = []
    # print(dept1)
    for iii in dept1:
        list1.append(iii[0])
        list2.append(iii[1])
        list3.append(iii[2])
    for iii in range(int(2 * t)):
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
    bm = ['第一集团', '第三集团', '集团'], ['业务群', '家族群', '相亲群'], ['业务线', '流水二线', '流水线'], ['事业部', '抹部', '情报部'], \
         ['交付部', '交付一部', '交付二部'], ['团队', '小队', '小分队', '二队', '三队', '应急队'], ['界', '动物界', '植物界', '微生物界'], \
         ['门', '脊索门', '脊椎亚门'], ['纲', '哺乳纲', '真兽亚纲', '今鸟亚纲', '鸟纲', '真兽亚纲'], ['目', '灵长目', '鸡形目', '裂脚亚目', '食肉目'], \
         ['科', '人科', '雉科', '犬科', '犬亚科'], ['属', '人属', '原鸡属', '犬属'], ['种', '智人种', '家鸡', '红原鸡', '家犬', '灰狼'], \
         ['军', '红军', '蓝军', '空军', '海军'], ['师', '暂七师', '八九师'], ['旅', '三八六旅', '野战旅'], \
         ['团', '独立团', '发面团', '新一团', '新一团'], ['营', '一营', '二营', '三营'], ['连', '警卫连', '钢七连', '红三连'], \
         ['排', '警卫排', '鸡排', '猪排'], ['班', '警卫班', '三班', '五班']
    bumen = bm[s3]
    chengpin = random.sample(s2, s1)
    shengcheng1 = []
    for i1 in chengpin:
        shengcheng1.append(i1 + random.choice(bumen))
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
print(list8)
result2 = result(list8, target2)
print(result2)
xie1(result2)


