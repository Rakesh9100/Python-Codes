>>> a=()
>>> type(a)
<class 'tuple'>

>>> a=tuple()
>>> type(a)
<class 'tuple'>
>>> a=()

>>> #HOMOGENEOUS OR HETEROGENEOUS
>>> a=(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> a=(10,20,11.1,222.3,"hello")
>>> a
(10, 20, 11.1, 222.3, 'hello')

>>> #Neseted Tuple
>>> a=(10,202,(31,3121,5946,59))
>>> a
(10, 202, (31, 3121, 5946, 59))
>>> print(a)
(10, 202, (31, 3121, 5946, 59))
>>> a=(10,20,[26,5654,97,898])
>>> a
(10, 20, [26, 5654, 97, 898])

>>> #Tuple Insertion and Deletion
>>> a=(10,20,30,40)
>>> a[2]
30
>>> #a[2]=60
>>> #a.append(50)
>>> #a.extend([10])
>>> #del a[2]
>>> #a[2]=60
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a
NameError: name 'a' is not defined

>>> #Inbuilt Methods
>>> a=(10,25,22,11)
>>> len(a)
4
>>> max(a)
25
>>> min(a)
10
>>> a.count(10)
1

>>> #Single Element Tuple
>>> a=(1)
>>> type(a)
<class 'int'>
>>> a=10,20,30
>>> a
(10, 20, 30)
>>> type(a)
<class 'tuple'>

>>> #Random
>>> import random
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> import random
>>> for i in range(10):
	print(random.randint(3,60))

	
54
24
41
3
16
11
50
38
7
9
