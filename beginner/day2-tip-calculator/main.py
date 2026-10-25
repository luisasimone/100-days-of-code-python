tot = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people? "))

to_pay = (tip / 100 * tot + tot) / people
print(f"Each person should pay: ${round(to_pay, 2)}")
