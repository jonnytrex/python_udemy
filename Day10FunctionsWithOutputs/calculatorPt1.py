



#Calculator


#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide 
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
  print(symbol)
operation_symbol = input("pick an operation from line above: ")
answer = operations[operation_symbol](num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")