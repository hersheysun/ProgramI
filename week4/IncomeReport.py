def main():
    incomes = []
    number_days = int(input("How many number_day? "))

    for mth in range(1, number_days + 1):
        income = float(input("Enter income for month " + str(mth) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    print_income(incomes, number_days, total)


def print_income(incomes, number_days, total):
    for mth in range(1, number_days + 1):
        income = incomes[mth - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(mth, income, total))


main()