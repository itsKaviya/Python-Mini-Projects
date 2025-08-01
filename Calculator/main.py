from art import logo

# calculator
def addition(n1,n2):     #add
  return n1+n2

def subtract(n1,n2):     #subtract
  return n1-n2

def multiply(n1,n2):  #multiply
  return n1*n2 

def divide(n1,n2):   #divide
  return n1/n2

operations= {
  "+":addition,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculation():
  print(logo)
  
  num1=float(input("What's the first number: "))
  for operand in operations:
    print(operand)
  
  to_continue = True
  while to_continue:
    operation_symbol=input("pick an operation: ")
    num2=float(input("What's the next number: "))
    operation_to_do=operations[operation_symbol]
    answer=operation_to_do(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    choice=input(f"Type 'y'to continue calculating with {answer},or type 'n'to start a new calculation : ")
    if choice == 'n':
      to_continue=False
      calculation()
    else:
      num1=answer

calculation()