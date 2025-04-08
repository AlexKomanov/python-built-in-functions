# iterable_1 = [True, False, False]
# iterable_2 = [False, False, False]
# iterable_3 = [True, True, True]

# print(any(iterable_1))
# print(any(iterable_2))
# print(any(iterable_3))

# Empty iterable returns False
# print(any([]))

# any() takes exactly one argument (0 given)
# print(any())

# Use case
# Check if at lest on ofthe elements 
# in a list is more than 18
# ages = [15, 22, 10, 17]
ages = [15, 8, 17, 12]

print(any(age > 18 for age in ages))  # True

if any(age > 18 for age in ages):
    print("At least one person is older than 18.")
else:
    print("No one is older than 18.")

