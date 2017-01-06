def function_name():
    pass
def file_reading(filename_local):
    filepointer = open(file_reading)
    for each in filepointer:
        print(each)
    filepointer.close()

def main():
    flag =True
    while(flag):
        try:
            filename=str(input(""))
            file_reading(filename)
            flag=False
        except FileNotFoundError:
            print("not exit")
            filename.close()