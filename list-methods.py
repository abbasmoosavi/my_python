numbers = [2 , 3, 8, 9, 12]
numbers.append(20)
print(numbers)
# [2, 3, 8, 9, 12, 20]

numbers = [2 , 3, 8, 9, 12]
numbers.insert(2, 20)
print(numbers)
# [2, 3, 20, 8, 9, 12]

numbers = [2 , 3, 8, 9, 12]
numbers.remove(8)
print(numbers)
# [2, 3, 9, 12]

numbers = [2 , 3, 8, 9, 12]
numbers.clear()
print(numbers)
# []

numbers = [2 , 3, 8, 9, 12]
numbers.pop()
print(numbers)
# [2, 3, 8, 9]

numbers = [2 , 3, 8, 9, 12]
print(numbers.index(8))
# 2

# numbers = [2 , 3, 8, 9, 12]
# print(numbers.index(50))
# ValueError: 50 is not in list

numbers = [2 , 3, 8, 9, 12]
print(50 in numbers)
# False

numbers = [2 , 3, 8, 9, 12]
print(numbers.count(8))
# 1


numbers = [2 , 10, 8, 4, 12, 7, 20]
numbers.sort()
print(numbers)
# [2, 4, 7, 8, 10, 12, 20]

numbers = [2 , 10, 8, 4, 12, 7, 20]
numbers.sort()
numbers.reverse()
print(numbers)
# [20, 12, 10, 8, 7, 4, 2]

numbers = [2 , 10, 8, 4, 12, 7, 20, 8, 3, 4, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
# [2, 10, 8, 4, 12, 7, 20, 3]

coordinates = (2, 5, 7)
x, y , z = coordinates
print(y)
# 5