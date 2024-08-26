for i in range(1,11):
    print(i)


'''
i is a variable that is assigned to each element
in the list that range returns
'''
'''
range is a function that returns a list of numbers
in the range specified as it's arguments when calling it
'''

'''
[1,2,3] is  of type list
range returns list
'''
print(list(range(19)))

for i in range(4):
    print("****")

for i in range(4):
    print('*'*i)
for i in range(4,0,-1):
    print('*'*i)
    
    
def contains_a(string):
    i = 0
    while i < len(string):
        if string[i] == 'a':
            return True
        i += 1
    return False


print(contains_a('hello'))
print(contains_a('america'))


