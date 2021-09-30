# Commit user input.
formula = input("your expression: ")
# Exclude whitespaces
formula = formula.replace(" ", "")
length = len(formula) - 1

# Error: user entered no expression.
if not formula:
    print("error, found no expression")
    exit(1)

# Check if there are numbers at the beginning and at the end of expression.
elif formula[0].isdigit() and formula[length].isdigit():
    while length >= 0:
        if formula[length].isdigit():
            length -= 1
        elif formula[length] == '+' or formula[length] == '-':
            # Error: more than one sign one after another.
            if formula[length + 1] == '+' or formula[length + 1] == '-':
                print("error in expression")
                exit(1)
            length -= 1
else:
    # Error: not numbers at the beginning and at the end of expression.
    print("error in expression")
    exit(1)

result = eval(formula)
print(" = ", result)