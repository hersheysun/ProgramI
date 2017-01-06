#new_list_comp=[each*2 for each in range(100)]
#print(new_list_comp)
from operator import itemgetter
FILENAME="books.csv"
file_list=[]


def print_header():
    print("""reading list 1.0{}books loaded from books.csv""")
def read_file():
    global file_list
    file_pointer= open(FILENAME,"r")
    for index, data in enumerate(file_pointer.readline()):
        data=data.strip()
        datum=data.split(",")
        print(index,datum)
        file_list.append(datum)
    file_list.sort(key=itemgetter(1,2))
    file_pointer.close()
read_file()