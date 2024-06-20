# Calculator Programme
def add(n1,n2):
   return n1 + n2
def subtract(n1,n2):
   return n1 - n2
def multiply(n1,n2):
   return n1 * n2
def divide(n1,n2):
   return n1 / n2

Operations ={
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide,
}

def calculator():
    end = False
    num_1 = float(input("What's your 1st number?: "))
    for symbols in Operations:
        print(symbols)
    while not end:
        type_operation = input("Pick and operation: ")
        num_2 = float(input("What's your next number?: "))
        calculation = Operations[type_operation]
        answer = calculation(num_1,num_2)
        print(f"{num_1} {type_operation} {num_2} = {answer}")
        again = input("If you want to continue type 'y' else type 'n' to start a new calculation : ")
        if again == "y":
           num_1 = answer
        if again == "n":
           calculator()
calculator()