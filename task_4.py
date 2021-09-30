# Recursive .
def bag(W, w, n):
    # No weights or capacity was entered as 0.
    if n == 0 or W == 0:
        return 0
    # Skip weights heavier than capacity.
    elif int(w[n - 1]) > W:
        return bag(W, w, n - 1)
    else:
        return max(w[n - 1] + bag(W - w[n - 1], w, n - 1), bag(W, w, n - 1))


# Commit user input.
try:
    capacity = int(input("capacity: "))
    weights = input("weights: ").split()
    for i in range(len(weights)):
        weights[i] = int(weights[i])
    print(bag(capacity, weights, len(weights)))
except:
    print("error")
