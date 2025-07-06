# Examples of the eval() function in Python
# What is eval() and why use it?
# eval() evaluates a string as a Python expression and returns the result.
# Use cases:
# - Dynamic code execution from user input
# - Parsing and evaluating mathematical expressions
# - Configuration files with Python expressions
# - Interactive calculators or formula evaluators
# WARNING: Never use eval() with untrusted input - it's a security risk!

# print("=== eval() Function Examples ===\n")

# 1. Mathematical expression
# print("1. Mathematical expression:")
# math_expr = "2 + 3 * 4"
# result = eval(math_expr)
# print(f"eval('{math_expr}') = {result}")
# print()


# 2. Print function 
# print("3. Print function:")
# eval("print('Hello from eval!')")
# print()

# 3. Configuration dictionary
# print("3. Configuration dictionary:")
# config = "{'host': 'localhost', 'port': 8080}"
# settings = eval(config)
# print(f"eval('{config}') = {settings}")
# print(f"Host: {settings['host']}, Port: {settings['port']}")
# print()

# 4. Incorrect syntax - not closed print
# print("4. Incorrect syntax example:")
# eval("print('Hello world'")  # Missing closing parenthesis


# 5. Complex expression that needs exec() instead of eval()
print("5. Complex expression (needs exec, not eval):")
eval("for i in range(3): print(i)")
print()

