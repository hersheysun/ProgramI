menu="1.get the odd number from array"+"\n""2.get the even number from array"+"\n""3.Show the squares from aray"+"\n""4.quit"
print(menu)
entry = int(input("select one function"+"\n"))

while (entry!=4):

    if entry==1:
        x= int(input("enter first number:"))
        y= int(input("enter last number:"))
        for i in range(x,y+1):
            if i%2 ==0:
                print (i,end='',)
            print()
            pass
    elif entry==2:
        x= int(input("enter first number:"))
        y= int(input("enter last number:"))
        for i in range(x,y+1):
            if i%2 !=0:
                print (i,end='')
            print()
            pass
    elif entry==3:
        x= int(input("enter first number:"))
        y= int(input("enter last number:"))
        for i in range (x, y+1):
            print(i ** 2, end=' ')
            print()
            pass
    else:
        print("we dont have the other function")
    print(menu)
    entry = int(input("select one function"+"\n"))
print("Thank you.")

