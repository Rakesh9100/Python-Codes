>>> #Empty List
>>> a=[]
>>> type(a)
<class 'list'>
>>> a=list()
>>> type(a)
<class 'list'>

>>> #List is homogeneous or heterogeneous
>>> a=[1,2,3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> a=[1,11.111,111.13,3.33]
>>> a
[1, 11.111, 111.13, 3.33]
>>> a=["assda","Assda",122,33.333]
>>> a
['assda', 'Assda', 122, 33.333]

>>> #Nested List
>>> a=[12,2131,13121,[32,132,1,132,1]]
>>> a
[12, 2131, 13121, [32, 132, 1, 132, 1]]

>>> #Accessing List
>>> a=[1,23,324,565]
>>> a[2]
324
>>> a[2:4]
[324, 565]
>>> a=[1,2,3,4,5,6]
>>> a[1:6:2]
[2, 4, 6]
>>> a[::-1]
[6, 5, 4, 3, 2, 1]

>>> #Matrices using list
>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a[1]
[4, 5, 6]
>>> a[1][2]
6

>>> # Clone list
>>> a=[1,2,3]
>>> b=a[:]
>>> b
[1, 2, 3]
>>> a=[10,20,30,40]
>>> a[0:4:2]
[10, 30]
>>> a[::-2]
[40, 20]
>>> mylist=[10,20,30,40]
>>> mylist[0:2]
[10, 20]
>>> mylist[0:4]
[10, 20, 30, 40]
>>> mylist[::1]
[10, 20, 30, 40]

>>> # In-built list
>>> a=[10,20,30,40]
>>> a.append(60)
>>> a
[10, 20, 30, 40, 60]

>>> #Append helps to add a new element at the last
>>> a.append([70,80])
>>> a
[10, 20, 30, 40, 60, [70, 80]]
>>> a.extend([80,90,100])
>>> a
[10, 20, 30, 40, 60, [70, 80], 80, 90, 100]

>>> # Insert
>>> a=[1,2,3,4]
>>> a.insert(2,10) ##Index position, element
>>> a
[1, 2, 10, 3, 4] 

>>> # Sort
>>> a=[161,64646,799,23,56794]
>>> a.sort()
>>> a=[23, 161, 799, 56794, 64646]
>>> a.sort(reverse=True)
>>> a
[64646, 56794, 799, 161, 23]
>>> a.sort(reverse=False)
>>> a
[23, 161, 799, 56794, 64646]

>>> #Delete
>>> a=[13,1646,64,6497,646]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[64,464,464,979]
>>> del a[2]
>>> a
[64, 464, 979]
>>> 
