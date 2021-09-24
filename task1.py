# 1-Create employee data excel file with duplicate record  that contain the fallowing field
# Emp id, Emp Name, Emp Salary
# Write a python code to display duplicate employee record and count no of duplicate record available into a employee data file.

import pandas as pd

try:
    employees = pd.read_excel('../employee test2.xlsx')
    # employees = pd.read_excel('../employee test.xlsx')
    df = pd.DataFrame(employees, columns = ['Emp id','Emp Name','Emp Salary'])
    duplicate = df[df.duplicated()]
    # data.drop_duplicates(subset=['Emp id','Emp Name','Emp Salary'], keep="first")

    if duplicate.size != 0:
        print("Duplicate Rows :")
        print(duplicate)
    else:
        print("Everything is unique")
except FileNotFoundError:
    print("File Not Found")
except:
    print("Error")