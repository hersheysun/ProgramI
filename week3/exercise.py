flag=True
while(flag):
    try:
        filename=input("what is file name: ")
        filepointer=open(filename)
        for each in filepointer:
            print(each)
        filepointer.close()
        flag=False
    except FileNotFoundError:
        print("the file does not exit")


