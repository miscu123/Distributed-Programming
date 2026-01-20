def numbers_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

def min_max(numbers):
    return min(numbers), max(numbers)

def even_numbers(numbers):
    counter = 0
    for number in numbers:
        if number % 2 == 0:
            counter += 1

    return counter