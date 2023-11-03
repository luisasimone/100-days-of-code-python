tot = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people? "))

tot_with_tip = tip / 100 * tot + tot
to_pay = tot_with_tip / people
print(f"Each person should pay: ${round(to_pay, 2)}")
