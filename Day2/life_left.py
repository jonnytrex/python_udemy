# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tot_days = 90*365
tot_weeks = 90*52
tot_months = 90*12
days = tot_days - int(age)*365
weeks = tot_weeks - int(age)*52
months = tot_months - int(age)*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")