programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

#add new items to dictionary

programming_dictionary["Loop"] = "A block of code that is repeated until a certain condition is met."
print(programming_dictionary)

#wipe an exisitng dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A flaw in a program."
print(programming_dictionary)  

#loop through a dictionary (it just gives you the keys)
for thing in programming_dictionary:
  print(thing)
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])