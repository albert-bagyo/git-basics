i = 8
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")
    
'''
% is the modulo operator
i % 2 is the remaider of i if divided by 2
'''

def evens(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

print(evens(range(10,100)))


def get_age():
    return int(input("What is your age? "))

age = get_age()
if age >= 60:
    print("You are old.")
else:
    print("You are fine.")
    
def get_age_by_year(current_year):
    date = int(input("What year were you born? "))
    if date < 0:
        print("Invalid date")
        return
    if date > current_year:
        print("You are not born yet")
        return
    age = current_year - date
    print(f"You are {age} years old.")
    
get_age_by_year(2023)

def leap_year():
    date = int(input("What year were you born? "))
    if date % 4 == 0:
        print('You were born in a leap year')
    else:
        print('Sorry you were not born in a leap year')

leap_year()
