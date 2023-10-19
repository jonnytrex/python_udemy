################### Scope ####################

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# not a good idea to use global inside function
# can use a return then assign the value to the global var.  eg return enemies =1 then enemies = increase_enemies()


  