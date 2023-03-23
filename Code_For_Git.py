print("Hello ShriSaran")
print("Hello jegan")


def sub(a, b):
    return a-b


# 2nd time file edited by JN
def add(A, B):
    C = A + B
    return C


# multiplication by Shrisaran
def mul(a, b):
    return a*b


def div(a, b):
    return a / b, a % b


# Power  by JN
def power(a, b):
    return a**b


X = int(input("Enter The First elements: "))
operation = input("Enter the operation to perform: ")
Y = int(input("Enter The second elements: "))
if operation == "+":
    print(f"The Added Value = {add(X,Y)}")
elif operation == "-":
    print(f"The subtraction Value = {sub(X,Y)}")
elif operation == "*":
    print(f"The multiplication Value = {mul(X,Y)}")
elif operation == "/":
    print(f"The division Value: quotient = {div(X,Y)[0]} remainder = {div(X,Y)[1]}")
elif operation == "^":
    print(f"The power value = {power(X, Y)}")
else:
    print("Invalid operation")
