'''
i = 0
while(i < 10):
    i = i + 1
    print(i)
'''
    
'''
This function prints every integer between from 1 to 9
'''

#The code snippet below prints even numbers between 12 and 20
'''
i = 12
while(i < 20):
    i = i + 2
    print(i)
'''

#Then upper bound is included
def evens(lower, upper):
    i = lower
    while(i < upper):
        i = i + 2
        print(i)
 
#The upper bound is excluded
def reverse_evens(lower, upper):
    i = upper
    while(i > lower):
        print(i)
        i = i - 2
        
        
evens(20, 40)
reverse_evens(20,40)