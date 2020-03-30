# pyodbc is an open source python module that makes accessing ODBC databases simple
# an ODBC driver uses the Open Database Connectivity (ODBC) interface by Microsoft
# allows applications to access data in database management systems (DBMS)
# using SQL as a standard for accessing the data
# pyodbc is an implementation of a driver that allows you to connect to any database

import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+password)

# a cursor itself is a control structure
# that allows use to control and manage rows of data from a response

class Dog():
    def bark(self):
        return 'rrrr'
Dog1 = Dog()
print(Dog1.bark())

# similar to class, you instantiate using cursor; data is fetched from Northwind
cursor = docker_Northwind.cursor()
cursor.execute('SELECT @@version')
#fetchall gets all record
row = cursor.fetchone()

print('The row is', row)

cust_rows = cursor.execute('SELECT * FROM Customers;').fetchone()
print('Customer rows are', cust_rows)


