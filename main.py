a = int(input("What is the value of a?"))
b = int(input("What is the value of b?"))
n = int(input("How many times would you like to iterate the multiplication of the numbers?"))
value = a*b
print(value, "is value without iteration")

for i in range(value*n):
    print(value,"is value with iteration")