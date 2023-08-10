# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h1 = float(height)
w1 = int(weight)
out = w1 / (h1 * h1)
# print(out)
output = str(out)
print(weight + " ÷ (" + height + " x " + height + ") = " + output)
print(int(out))