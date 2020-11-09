numbers = [2, 2, 3, 4, 6, 3, 6, 1, 7, 1]
uniques = []
numbers.sort()
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
