from functools import reduce

def even_number(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
            
    return result


numbers = [1,56,234,87,4,76,24,69,90,135]
print(even_number(numbers))


def is_even(number):
    return number % 2 == 0

def even_numbers_with_map_and_filter(numbers:list[int]) -> list[int]:
    return list(map(is_even,numbers))

def even_numbers_with_map_filter_and_lambda(numbers:list[int]) -> list[int]:
    return list(filter(lambda x: x != None,map(is_even, numbers)))

def odd_numbers(numbers:list[int]) -> list[int]:
    return list(filter(lambda x: not is_even(x), numbers))

def join_strings(strings):
    return reduce(lambda joined, x: joined + x, strings)

print(even_numbers_with_map_and_filter(numbers))
print(even_numbers_with_map_filter_and_lambda(numbers))
print(odd_numbers(numbers))
print(join_strings(['hello', ' world', ' something', ' here']))

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
numbers2 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
words = ["hello", "my", "name", "is", "Sam"]


print([n for n in numbers if n > 0])
print([n for n in numbers2 if n % 2 == 0])
print([(word.capitalize(), len(word)) for word in words])