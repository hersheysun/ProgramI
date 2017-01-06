
lower = 10
upper = 50
a = input("Enter a number (%s-%s): " % (lower, upper))
def change(a) :
    if a.isdigit() and lower < int(a) < upper:
        print("Ascii character is:", chr(int(a)))
    else:
        print("Please enter a valid number!")
print(change(a))