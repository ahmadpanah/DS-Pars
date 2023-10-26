import string
import random


characters = list(string.ascii_letters + string.digits + "!@$%^*")

def generate_password():
    password_lenght = int(input("How Long Would you like your password?"))

    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No)")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended.")
    quit()
else:
    print("Invalid Input")
    quit()
