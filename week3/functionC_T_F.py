def get_temp():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_to_farenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Farenheit:"))
            convert_to_Celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_Celsius(fahrenheit):
    try:
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} F".format(celsius))
    except ValueError:
        print("ERROR.")


def convert_to_farenheit(celsius):
    try:
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} C".format(fahrenheit))
    except ValueError:
        print("ERROR.")


get_temp()