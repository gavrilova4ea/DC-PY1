list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
max_ = list_numbers[max_index]

for i, index in enumerate(list_numbers):
    max_ = list_numbers[max_index]
    if index > max_:
        max_index = i
        max_ = list_numbers[max_index]

list_numbers[9], list_numbers[19] = list_numbers[19], list_numbers[9]
print(list_numbers)
