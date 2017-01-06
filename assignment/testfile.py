import csv
from operator import itemgetter

print("Reading List 1.0 - by Hexu \n4 books loaded from books.csv")
FILENAME = "books.csv"
#file_list = []
def get_choice():
    MENU = "R - List required books \nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "1":
        if choice =="R":
            try:
                dataitems = []
                file_pointer= open(FILENAME, "r")

                for index, data in enumerate(file_pointer.readlines()):
                    data = data.strip()
                    datum = data.split(",")
                    print(index, datum)
                    dataitems.append(datum)

                    totalpages = 0                                   #sum?
                for row in dataitems:
                    totalpages += int(row[2])
                    print("total pages of ",index,"book is",totalpages)
                file_pointer.close()

                read_file()

            except ValueError:
                print("enter a choice from menu")
        elif choice =="C":
            try:
                with open(FILENAME, 'r') as file_handle:
                    reader = csv.reader(file_handle)
                    for row in reader:
                        if row[3] == 'c':
                            print (row)

            except ValueError:
                print("enter a choice from menu")

        elif choice =="A":
            try:
                bookname= str(input("enter book name:"))
                author=str(input("enter author name:"))

                state= str(input("enter state of book"))
                try:
                    pages= int(input("enter book pages:"))
                    return true
                    if pages<=0:
                        raise Exception("invalid number")
                        print("number must be bigger than 0")
                except ValueError:
                    print("Invalid input; enter a valid number")
                if author.strip()=='':
                    print("Input can not be blank")

                csvfile = open(FILENAME, 'wb')
                fieldnames=['bookname','author','page','state']
                writer = csv.writer(csvfile,fieldnames=fieldnames)
                writer.writerow({'bookname':'bookname','author':'author','pages':'pages','state':'state'})
                data = [('bookname', 'author', 'pages','state') ]
                writer.writerows(data)
                print("Code Complete by",author,pages,"added to reading list")
                csvfile.close()
            except ValueError:
                print("enter a choice from menu")

            print("Code Complete by"+author,pages+"added to reading list")
"""
        elif choice =="M":
            try:

                with open(FILENAME, 'r') as file_handle:
                    reader = csv.reader(file_handle)
                    print("required books:\n")
                    for row in reader:
                        if row[3] == 'r':
                            print (row)
                    for row in dataitems:
                        totalpages += int(row[2])
                        print("total pages of ",index,"book is",totalpages)
                        file_pointer.close()


            except ValueError:
                print("enter a choice from menu")



        elif choice =="Q":

            print(index,"books saved to books.csv")
        else:
            print(MENU)
        print("thank you")
"""
get_choice()