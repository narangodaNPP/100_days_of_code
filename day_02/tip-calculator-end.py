print("Welcome to the tip clculator.")
#If the bill was $150.00, split between 5 people, with 12% tip. 
input_bill = input("What was the total bill? ")
input_amount = input("How many people to split the bill? ")
percentage = input("What percentage to tip would you like to give? 10, 12, or 15: ")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
each_person = float(input_bill)/ float(input_amount)
#Format the result to 2 decimal places = 33.60
each_person_bill = each_person * (100+int(percentage))/100 + each_person
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print(f"Each person should pay: ${each_person_bill:.2f}")
#Write your code below this line 👇