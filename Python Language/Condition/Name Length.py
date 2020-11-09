name = input("Please enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters.")

elif len(name) > 40:
    print("Name must be a maximum of 40 characters.")

else:
    print("Name looks good!")