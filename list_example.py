numbers = [2, 3, 5, 7, 11, 13]
names = ["John", "Tom", "Kane", "Son"]

n = 2
m = 4

print(names[n:m])
print(len(numbers))
print(numbers)
numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))
del numbers[2]
print(numbers)
numbers.insert(4,50)
print(numbers)

print(sorted(numbers))
numbers.sort(reverse = True)
print(numbers)

for number in numbers:
   print(number)