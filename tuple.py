def partition(number):
    if number % 2 == 0:
        return number , None
    else:
        return None, number
    
def partition_list(l):
    odds = []
    evens = []
    for number in l:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds


print(partition(20))
print(partition_list(range(0,15)))