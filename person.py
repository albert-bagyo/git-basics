def get_age():
    return int(input("What is your age? "))


def get_name():
    return input("What is your name? ")

name = get_name()
age = get_age()

print(f"Hi, {name} you are {age} years old")
