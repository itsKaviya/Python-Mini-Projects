print("welcome to tip calculator")
bill=float(input("what was the total bill? $"))
tip_percentage=int(input("what percentage tip would you like to give? 10,12 or 15? "))
no_of_people=int(input("how many people to split the bill? "))

tip=tip_percentage/100
net_bill=bill+(bill*tip)
individual_payment=net_bill/no_of_people
rounded_payment=round(individual_payment,2)

print(f"Each person should pay: ${rounded_payment}")