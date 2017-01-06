
import csv
dataitems=[] #global varibles


def read_file():
                    file_pointer= open(FILENAME, "r")
                    for index, data in enumerate(file_pointer.readlines()):
                        data = data.strip()
                        datum = data.split(",")
                        print(index, datum)
                        dataitems.append(datum)                                                                                   #{}
                    totalpages = 0                                   #sum?
                    for row in dataitems:
                        totalpages += int(row[2])
                    print("total pages of ",index,"book is",totalpages)
                    file_pointer.close()

def write_file():
                    with open(FILENAME, 'r') as file_handle:
                        reader = csv.reader(file_handle)
                        print("required books:\n")
                        for data in reader:
                            if data[3] == 'r':
                                print (data)
                        dataitems = []
                        file_pointer= open(FILENAME, "r")

                        for index, data in enumerate(file_pointer.readlines()):
                            data = data.strip()
                            datum = data.split(",")
                            dataitems.append(datum)
                        totalpages=0
                        for row in dataitems:
                            totalpages += int(row[2])
                            print("total pages of ",index,"book is",totalpages)
                    write_file.close()

print("Reading List 1.0 - by Hexu \n4 books loaded from books.csv")
FILENAME = "books.csv"
#file_list = []

MENU = "R - List required books \nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ (for quit)"
running= True
print("Reading List 1.0 - by Hexu \n4 books loaded from books.csv")
while running:


        print(MENU)
        choice = input(">>> ").upper()

        if choice =="R":
            try:
                 read_file()
            except FileNotFoundError:
                print("cant not find your file")



        elif choice =="C":
            try:
                with open(FILENAME, 'r') as file_handle:
                    reader = csv.reader(file_handle)
                    for data in reader:
                        if data[3] == 'c':
                            print (data)

            except ValueError:
                print("enter a choice from menu")


        elif choice =="A":
            try:
                bookname= input("enter book name:")
                author=input("enter author name:")
                if author.strip()=='':
                    print("Input can not be blank")
                try:
                    pages= int(input("enter book pages:"))

                    if pages<=0:
                        raise Exception("invalid number")
                        print("number must be bigger than 0")
                except ValueError:
                    print("Invalid input; enter a valid number")

                csvfile = open(FILENAME, 'a')                                      #insert?
                csvfile.write(bookname+","+author+","+str(pages)+","+"r")
                csvfile.close()

            except ValueError:
                print("enter a choice from menu")


        elif choice =="M":
            try:
                read_file()
                print("Enter the number of a book to mark as completed")
            except ValueError:
                print("enter a choice from menu")



        elif choice =="Q":
            print("books saved to books.csv")
            print("program finish, have a nice day ")
            running=False
        else:
            print("enter a choice from menu")

print("thank you")

