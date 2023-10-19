def main():
    print("Welcome to email Slicer!")
    print("")

    email_input = input("Input your email address: ")

    # hossein@gmail.com
    (username , domain) = email_input.split("@")
    (domain, extension) = domain.split(".") 

    print("Username is: " , username)
    print("Domain is: ", domain)
    print ("Extension is: ", extension)


while True:
    main()