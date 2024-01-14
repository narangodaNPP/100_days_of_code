#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
each_person = round((float(bill)/int(people)) * ((float(tip)+100)/100), 2)
#Format the result to 2 decimal places = 33.60
print(f"Each person should pay: {each_person:.2f}")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇