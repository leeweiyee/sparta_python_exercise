# Create and read an excel file using openpyxl and xlsxwriter libraries
# At terminal type: pip3 install openpyxl and pip3 install xlsxwriter

# Create excel file using python
import xlsxwriter

# create workbook using built-in method and assigning a name to the file
data9 = xlsxwriter.Workbook('data9.xlsx')

# create an object
worksheet = data9.add_worksheet('All students')

# change the name of a worksheet:
worksheet.name = 'Trainees'

# note: rows and columns are 0 indexed
# first cell in worksheet A1 is (0,0), B1 is (0,1)

# use  builtin write method to insert data to our file
# worksheet.write("A1", "Data 9")
# worksheet.write("A2", "Andy")
# worksheet.write("A3", "Ben")
# worksheet.write("A4", "CJ")
# worksheet.write("A5", "Gigi")
# worksheet.write("A6", "Johnny")
# worksheet.write("A7", "Khanhi")
# worksheet.write("A8", "Sassy")
# worksheet.write("A9", "Shugs")
# worksheet.write("A10", "Tosin")
# worksheet.write("A11", "Vivek")
# worksheet.write("A12", "Weiyee")
# worksheet.write("A13", "Yin")

# efficient way to insert names under data 9 column
row = 0
column = 0
content = ["First Name", "Andy", "Ben", "CJ", "Gigi", "Johnny", "Khanhi", "Sassy", "Shugs", "Tosin", "Vivek", "Weiyee", "Yin"]
for name in content:
    # worksheet.write("A1", "Data 9")
    worksheet.write(row, column, name)
    row += 1 # increment row by 1 with each iteration

# saves and creates excel file
data9.close()


