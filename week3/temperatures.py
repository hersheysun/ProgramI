MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        try:
            a = float(input("Celsius: "))
            celsius=a
            if celsius < -275:
                raise Exception("invalid")
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        except ValueError:
            print("it is not a number!")
        except:
            print("Please enter a valid number!")
    elif choice == "F":
        try:
            fahrenheit = float(input("Celsius: "))

            celsius = (fahrenheit -32)*5/9
            print("Result: {:.2f} F".format(celsius))
        except ValueError:
            print("it is not a number!")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")