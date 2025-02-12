print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?: "))
percentage = int(input("What percentage tip would you like to give? 10 or 12 or 15: "))
people = int(input("How many people to split the bill?  "))
amount = bill * (percentage / 100 + 1)
amount_forEach = amount / people
result = round(amount_forEach, 2)
print(f"Each person should pay: ${result}")
