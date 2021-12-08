>>> # PICKLING - To dump the file or dump the entire collection using

>>> #FILE HANDLING

>>> import pickle
>>> f=open("demo.pkl","wb") #pkl = pickle extension, wb=write binary
>>> data=[1,2,3]
>>> pickle.dump(data,f)
>>> f.close()
>>> print("The file has been successfully dumped")
The file has been successfully dumped

>>> f=open("demo.pkl","rb")  #rb = read binary
>>> read=pickle.load(f)
>>> f.close()
>>> print("The content of the dumped file is: ")
The content of the dumped file is: 

>>> f.read()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f.read()
ValueError: read of closed file   ## File is closed so not readable and error is coming

>>> f=open("demo.pkl","rb")
>>> read=pickle.load(f)
>>> print("The content of the dumped file is: ")
The content of the dumped file is: 
>>> f.read()
b''

>>> #EXCEPTION HANDLING
>>> #ERROR
>>> # Unlogical structures which causes the interruption of program

>>> # Types of error
>>> #1. Compile Time error
>>> #2. Run Time error
>>> # Compile : Syntax
>>> # Indendation - Compile Time error
>>> # Primary definition of Exception : Runtime error

>>> a=5
>>> b=0
>>> c=a/b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c=a/b
ZeroDivisionError: division by zero

>>> # This is Exception or Runtime error
>>> a=[]
>>> print(a[3])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a[3])
IndexError: list index out of range

>>> a={}
>>> print(a["abc"])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(a["abc"])
KeyError: 'abc'

>>> # Exception handling
>>> ## try - code which may cause error
>>> ## except - catch the error

>>> filename=input("Enter the filename: ")
Enter the filename: demo

>>> ## LIST OF EXCEPTIONS
>>> 1	
Exception

Base class for all exceptions

2	
StopIteration

Raised when the next() method of an iterator does not point to any object.

3	
SystemExit

Raised by the sys.exit() function.

4	
StandardError

Base class for all built-in exceptions except StopIteration and SystemExit.

5	
ArithmeticError

Base class for all errors that occur for numeric calculation.

6	
OverflowError

Raised when a calculation exceeds maximum limit for a numeric type.

7	
FloatingPointError

Raised when a floating point calculation fails.

8	
ZeroDivisionError

Raised when division or modulo by zero takes place for all numeric types.

9	
AssertionError

Raised in case of failure of the Assert statement.

10	
AttributeError

Raised in case of failure of attribute reference or assignment.

11	
EOFError

Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

12	
ImportError

Raised when an import statement fails.

13	
KeyboardInterrupt

Raised when the user interrupts program execution, usually by pressing Ctrl+c.

14	
LookupError

Base class for all lookup errors.

15	
IndexError

Raised when an index is not found in a sequence.

16	
KeyError

Raised when the specified key is not found in the dictionary.

17	
NameError

Raised when an identifier is not found in the local or global namespace.

18	
UnboundLocalError

Raised when trying to access a local variable in a function or method but no value has been assigned to it.

19	
EnvironmentError

Base class for all exceptions that occur outside the Python environment.

20	
IOError

Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

21	
OSError

Raised for operating system-related errors.

22	
SyntaxError

Raised when there is an error in Python syntax.

23	
IndentationError

Raised when indentation is not specified properly.

24	
SystemError

Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.

25	
SystemExit

Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.

26	
TypeError

Raised when an operation or function is attempted that is invalid for the specified data type.

27	
ValueError

Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.

28	
RuntimeError

Raised when a generated error does not fall into any category.

29	
NotImplementedError

Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
>>> 
>>> 2+"5"
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    2+"5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> 3>"s"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    3>"s"
TypeError: '>' not supported between instances of 'int' and 'str'
