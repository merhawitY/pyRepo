def userinfo():
    name = input("What is your name? ")
    lastname = input("What is your last name? ")
    age = int(input("What is your age? "))

    return f"{name} {lastname} {age}"

user = userinfo()

print(user)