# Import needed elements of modules.
from operator import add, sub, mul, truediv
from sys import argv

# Check if all arguments are present.
if len(argv) == 4:
    dictionary = {'+': add, '-': sub, '*': mul, '/': truediv}
    # Replace sign if it's present in the dictionary.
    try:
        print(dictionary[argv[2]](int(argv[1]), int(argv[3])))
    except:
        print("error")
else:
    print("not enough arguments")