username=str(input("what is your name: "))


try:
    file_object = open('name.txt','w')
    file_object.write(username)
    file_object.close( )
except FileNotFoundError:

    file_object = open('numbers.txt','r')
    total={float(line) for line in file_object.readline()}
    file_object.close()
    a=sum(total)

finally:

    print("your name is ",username)

