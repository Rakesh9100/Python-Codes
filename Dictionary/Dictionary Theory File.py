>>> #Empty Dictionary
>>> a={}
>>> type(a)
<class 'dict'>
>>> a=dict(a)
>>> type(a)
<class 'dict'>
>>> a={1:"Sam", 2:"Ram"}
>>> a
{1: 'Sam', 2: 'Ram'}
>>> a={"Sam":20, "Ram":30}
>>> a
{'Sam': 20, 'Ram': 30}
>>>
>>> #Insertion and Deleting inside Dictionary
>>> a={1:"Sam", 2:"Ram"}
>>> a[3]="Shyam"
>>> a
{1: 'Sam', 2: 'Ram', 3: 'Shyam'}
>>> a.update({4:"John"})
>>> a
{1: 'Sam', 2: 'Ram', 3: 'Shyam', 4: 'John'}
>>> del a[3]
>>> a
{1: 'Sam', 2: 'Ram', 4: 'John'}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a={1:'R', 2:'Sh', 3:'RO'}
>>> a.clear()
>>> a
{}
>>> a.pop
<built-in method pop of dict object at 0x000001E2FF24EF80>
>>>
>>> ##Inbuilt Functions
>>> mydict={1:'Sam', 2:'Ram', 3:'Shyam', 4:'John'}
>>> mydict.keys()
dict_keys([1, 2, 3, 4])
>>> mydict.values()
dict_values(['Sam', 'Ram', 'Shyam', 'John'])
>>> mydict.items()
dict_items([(1, 'Sam'), (2, 'Ram'), (3, 'Shyam'), (4, 'John')])
>>>
>>> #Uniqueness
>>> dict={0:10, 1:20}
>>> dict[2]=30
>>> dict
{0: 10, 1: 20, 2: 30}
>>>
