#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
total_bill = input("What was the total bill? ")
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_amount = float(total_bill) * int(percent_tip)/100
each_pay = round((float(total_bill) + tip_amount) / int(people),2)
# format to print 2 decimal places 
each_pay = "{:.2f}".format((float(total_bill) + tip_amount) / int(people))
print(f"Each person should pay: ${each_pay}")
