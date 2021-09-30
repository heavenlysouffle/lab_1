# Import needed elements of modules.
from sys import argv
from operator import add, sub, mul, truediv

# Check if all arguments are present.
if len(argv) == 4:
    dictionary = {'add': add, 'sub': sub, 'mul': mul, 'div': truediv}
    # Replace sign if it's present in the dictionary.
    try:
        print(dictionary[argv[1]](int(argv[2]), int(argv[3])))
    except:
        print("error")
else:
    print("not enough arguments")
