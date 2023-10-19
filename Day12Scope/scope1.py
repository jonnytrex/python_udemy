################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

# global scope

player_health = 10
def drink_potion2():
  potion_strength = 2
  print(player_health)

drink_potion2()

