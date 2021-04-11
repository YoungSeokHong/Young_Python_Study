# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
first_name = name_data[0]
last_name = name_data[1]
print(first_name, last_name)

numbers = "\n\n    2  \t   \n3\n   5    7\n    11".split()
print(int(numbers[0]) + int(numbers[1]))
print(numbers)