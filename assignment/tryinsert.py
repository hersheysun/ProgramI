import csv

FILENAME = "books.csv"
from operator import itemgetter
FILENAME = "books.csv"

def read_file():
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