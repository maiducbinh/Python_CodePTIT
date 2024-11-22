# This Python code snippet is checking if the input string ends with ".py" in a case-insensitive
# manner. Here's a breakdown of what the code does:
s = input()
if s[-3:].lower() == '.py':
    print("yes")
else:
    print('no')