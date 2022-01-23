import random

list1 = ['jituan1', 'jituan2', 'jituan3']
list2 = ['yewuqun1', 'yewuqun2', 'yewuqun3', 'yewuqun4', 'yewuqun5']
while len(list2) > len(list1):
    list1.append(random.choice(list1))
print(list1)
random.shuffle(list1)
random.shuffle(list2)
dict1 = zip(list2, list1)
# dict2 = {'业务群1': '集团1', '业务群2': '集团2'}
# dict2.update(dict1)
print(dict1)
