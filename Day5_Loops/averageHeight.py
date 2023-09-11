# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
n = 0
total = 0
for height in student_heights:
    total = total + height  
    # use total += height
    n = n+1
    # use n += 1
average = total / n
print(round(average))
