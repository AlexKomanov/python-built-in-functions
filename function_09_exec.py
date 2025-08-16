
print("=== exec() Function Example ===\n")

# exec() can execute a block of code contained in a string.
# Variables and functions defined in that string are added
# to the current scope, making them available afterwards.

# 1. Basic single-line example
# print("1. Basic single-line example:")
# exec("print('Hello from exec!')")
# print()

# # 2. Multi-line example
# print("2. Multi-line example:")
# source_code = """
# a = 10
# b = 20
# print(f"Inside exec: a + b = {a + b}")

# for i in range(3):
#     print(f"Inside exec loop: {i}")
# """

# exec(source_code)

# print()

# # 3. Accessing variables defined in the string
# The variable 'a' was defined inside the 'source_code' string
# and is now accessible in the global scope because of exec().
# print("3. Accessing variable 'a' after exec():")
# try:
#     print(f"The value of 'a' is: {a}")
# except NameError as e:
#     print(f"Error accessing 'a': {e}")

# 4. exec() returns None, unlike eval() which returns a value
print("\n4. exec() return value:")
result = exec("print('This is executed by exec()')")
print(f"exec() returned: {result}")

