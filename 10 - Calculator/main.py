import os
from art import logo

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def display_result(choice, n1, n2, result):
  print(f"\n\t\t{n1} {choice} {n2} = {result}")

def check_choice(choice, n1, n2):
  result = 0
  for check in operations:
    if check == choice:
      result = operations[check](n1, n2)
      display_result(choice, n1, n2, result)
      return result

def calling_functions(result, repeat):
  if repeat == "yes":
    n1 = result
    choice = input("\n\n\t\t'+ - * /'\n\nChoose an operator : ")
    n2 = float(input(f"Enter a number : {n1} {choice}  "))
  else:
    cls()
    print(logo,"\n\n\n")
    n1 = float(input("Enter first number : "))
    n2 = float(input("Enter second number : "))
    choice = input("\n\n\t\t'+ - * /'\n\nChoose an operator : ")
    
  result = check_choice(choice, n1, n2)

  return result

repeat = ""
result = 0
while repeat != "q":
  result = calling_functions(result, repeat)
  repeat = input("\n\nEnter 'yes', if you want to further process the answer.\nEnter 'no', if you want to start over.\nEnter 'q' to exit\nEnter your choice : ").lower()
  if repeat == "q":
    print("\n\n\t\t\tGood Bye!")
  print("\n\n")