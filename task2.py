# 2- Search and count the word available in file. 

try:
    word = input("serach word:")

    #get file object reference to the file
    file = open("../tasks.txt", "r")

    #read content of file to string
    data = file.read()

    #get number of occurrences of the substring in the string
    occurrences = data.count(word)

    print('Number of occurrences of the ',word,' :', occurrences)
except FileNotFoundError:
    print("File Not Found")
except:
    print("Error")