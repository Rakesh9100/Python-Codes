>>> import keyword

>>> keyword.iskeyword("sample")
False

>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36

>>> 7+3
10

>>> a=10000000000000
>>> a
10000000000000

>>> 3+2
5

>>> 3-2
1

>>> 3*3
9

>>> 2/3
0.6666666666666666

>>> 2//3
0

>>> 2%3
2

>>> 4//2
2

>>> 4/2
2.0

>>> 2**3
8

>>> #PEMDAS
>>> #P=Paranthesis
>>> #E-Exp
>>> #M-Mul
>>> #D-Div
>>> #A-Add
>>> #S-Subt

>>> a='hi'
>>> b='everyone'
>>> a+b
'hieveryone'

>>> a+''+b
'hieveryone'

>>> a+' '+b
'hi everyone'

>>> a='fun'
>>> a*3
'funfunfun'

>>> 'fun'*3
'funfunfun'

>>> b='fun'*3
>>> print (b)
funfunfun

>>> (7*3600)+(21*60)+37
26497

>>> a=7
>>> b=21
>>> c=37
>>> d=(a*3600)+(b*60)+c
>>> d
26497

>>> length=4
>>> width=7
>>> perimeter=2*(length+width)
>>> perimeter
22

>>> rad=8
>>> pi=3.14
>>> circum=2*pi*rad
>>> circum
50.24

>>> rad=8
>>> pi=3.14
>>> area=pi*rad*rad
>>> area
200.96

>>> p=1000
>>> r=7
>>> y=10
>>> value=p*(1+(0.01*r))*y
>>> value
10700.0

>>> str='Joe Warren is'
>>> a='52'
>>> str1='years old.'
>>> value=str+' '+a+' '+str1
>>> value
'Joe Warren is 52 years old.'

>>> str1="My name is"
>>> str2="Joe"
>>> str3="Warren"
>>> value=str1+' '+str2+' '+str3
>>> value
'My name is Joe Warren'

>>> x0=2
>>> y0=2
>>> x1=5
>>> y1=6
>>> value=((x0-x1)*(x0-x1))+((y0-y1)*(y0-y1))
>>> value
25
