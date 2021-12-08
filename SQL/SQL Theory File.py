>>> import mysql.connector
>>> host="localhost",

>>> import mysql.connector
>>> mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="admin"
	)
>>> print(mydb)
<mysql.connector.connection_cext.CMySQLConnection object at 0x0000028284C8BF40>

>>> #How to create a database

>>> import mysql.connector
>>> mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="admin"
	)
>>> mycursor=mydb.cursor()
>>> mycursor.execute("CREATE DATABASE RAKESH")
>>> print("Database has been successfully created")
Database has been successfully created

>>> #How to check the available databases

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
host="localhost",
user="root",
password="admin"
)
>>> mycursor=mydb.cursor()
>>> mycursor.execute("SHOW DATABASES")
>>> for x in mycursor:
	print(x)

	
('information_schema',)
('mysql',)
('performance_schema',)
('rakesh',)
('sakila',)
('sys',)
('world',)

>>> #How to check whether database is connected or not

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="rakesh"
)

>>> #How to create a table in the database

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="rakesh"
)
>>> mycur=mydb.cursor()
>>> mycur.execute("CREATE TABLE Student(name VARCHAR(255),address VARCHAR(255))")
>>> print("Table has been successfully created")
Table has been successfully created

>>> #How to check whether the table is created or not

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
host="localhost",
user="root",
password="admin",
database="rakesh"
)
>>> mycur=mydb.cursor()
>>> mycur.execute("SHOW TABLES")
>>> for x in mycur:
	print(x)

	
('student',)

>>> #How to create a primary key and autoincrement

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host="localhost",
user="root",
password="admin",
database="rakesh"
)
>>> mycur=mydb.cursor()
>>> mycur.execute("CREATE TABLE Customer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),address VARCHAR(255))")
>>> print("Table has been successfully created")
Table has been successfully created

>>> # How to modify the existing table

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="admin",
	database="rakesh"
	)
>>> mycur=mydb.cursor()
>>> mycur.execute("ALTER TABLE Customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
>>> mycur.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
>>> print("Table has been successfully modified")
Table has been successfully modified
 
>>> #How to insert the data in the table of the database

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="admin",
	database="rakesh"
	)
>>> mycur=mydb.cursor()
>>> sql="INSERT INTO student(name,address)VALUES(%s,%s)"
>>> val=("sdp","Punjab")
>>> mycur.execute(sql,val)
>>> mydb.commit()
>>> print(mycur.rowcount,"Records inserted in the table")

1 Records inserted in the table
