print("electricity bill estimator")

centper = float(input("Enter the cent per: "))
dailyuse =float(input("Enter the daily use:"))
day=int(input("Enter the day:"))
Estimated= (centper*0.01)*dailyuse*day
print(centper,"kWh")
print(dailyuse,"kWh")
print(day,"kWh")
print(Estimated)
