def calculate(string, first_int, second_int):
    operation = string.lower()
    if operation == 'add':
        return first_int + second_int
    
    elif operation == 'subtract':
        return first_int - second_int
    
    elif operation == 'multiply':
        return first_int * second_int
    
    elif operation == 'divide':
        return first_int / second_int
    
    else:
        print("That operation does not exist.")


print(calculate('add',2,3))
print(calculate('subtract',2,3))
print(calculate('multiply',2,3))
print(calculate('divide',2,3))
        
        