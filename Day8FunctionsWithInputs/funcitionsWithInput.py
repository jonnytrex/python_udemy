# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("How are you?")
  print("Goodbye")  

greet()

# Function that allows for input

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you {name}?")
  print(f"Goodbye {name}")

greet_with_name("Jon")

# functions with more that 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with("Jon", "New York")

# functions with keyword args

greet_with(location="New York", name="Jon")