my_dict = {'1':['a','b'], '2':['c','d']}
list1 = my_dict['1']
list2 = my_dict['2']
l1 = len(list1)
l2 = len(list2)
for j in range(0,l1):
    for i in range(0,l2):
        print(list1[j]+list2[i])
