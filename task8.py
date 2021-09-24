# 8-Write a program to read each row from a given csv file and print a list of strings.
import csv
try:
    with open('../departments.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in data:
            print(', '.join(row))
except FileNotFoundError:
    print("File Not Found")
except:
    print("Error")