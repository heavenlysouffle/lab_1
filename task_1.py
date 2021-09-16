# Import needed elements of modules.
from sys import argv
from operator import add, sub, mul, truediv

# Check if all arguments are present.
if len(argv) == 4:
    dictionary = {'+': add, '-': sub, '*': mul, '/': truediv}
    # Replace sign if it's present in the dictionary.
    print(dictionary[argv[2]](int(argv[1]), int(argv[3])))
