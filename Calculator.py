def add(a,b):
    answer = a+b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + " = " + str(answer))

def div (a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + " = " + str(answer))

print("A. Addition")
print("B. Substraction")
print("C. Multiplaction")
print("D. Division")
print("E. Exit")

choice = input("Please enter your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Please Enter 1st number: "))
    b = int(input("Please Enter 2st number: "))
    add(a,b)
elif choice == "b" or choice == "B":
    print("Substraction")
    a = int(input("Please Enter 1st number: "))
    b = int(input("Please Enter 2st number: "))
    sub(a,b)
elif choice == "c" or choice == "C":
    print("Multipliction")
    a = int(input("Please Enter 1st number: "))
    b = int(input("Please Enter 2st number: "))
    mul(a,b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Please Enter 1st number: "))
    b = int(input("Please Enter 2st number: "))
    div(a,b)
elif choice == "e" or choice == "E":
    print("Thank You ♥")
    quit()

    