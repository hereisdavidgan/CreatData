import csv
dict1 = {'业务群1': '集团1', '业务群2': '集团2', 'yewuqun5': 'jituan2', 'yewuqun2': 'jituan3', 'yewuqun4': 'jituan1', 'yewuqun1': 'jituan1', 'yewuqun3': 'jituan1'}
list1 = list(dict1.keys())
list2 = list(dict1.values())
print(list1)
print(list2)

f = open('../csv/1.md', mode='w', encoding='UTF-8')
f.write('```mermaid\n')
f.write('graph TD;\n')
for i in range(len(dict1)):
    a = list2[i]
    b = '-->'
    c = list1[i]
    d = ';\n'
    f.write(a + b + c + d)
f.write('```\n')
f.close()
