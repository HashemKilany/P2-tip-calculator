#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip =float(input("How much tip would you like to give?"))
persons_no = int(input("How many people to split the bill?")) 
result = (bill*float(1+tip/100))/persons_no
print (f"Each person should pay: {round(result,2)}$")