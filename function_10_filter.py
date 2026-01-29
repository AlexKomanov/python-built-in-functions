# filter() - filters elements from an iterable based on a function

# Example 1: Using a regular function
# names: list[str] = ['James', 'John', 'Jam', 'Bob']


# def starts_with_j(name: str) -> bool:
#     return name[0].lower() == 'j'


# j_names: filter = filter(starts_with_j, names)
# print(list(j_names))


# Example 2: Using a lambda function
names: list[str] = ['Alex', 'Anna', 'Jam', 'Bob']

a_names: filter = filter(lambda s: s[0].lower() == 'a', names)
print(list(a_names))
