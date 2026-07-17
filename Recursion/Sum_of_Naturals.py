def recursiveSummation(val):
    # base case / stopping point
    if val <= 1:
        return val

    # recursive call / problem space shrinkage
    return val + recursiveSummation(val - 1)


print(recursiveSummation(5))