def findBinary(val, result):
    if val == 0:
        return result

    result = str(val % 2) + result

    return findBinary(val // 2, result)


print(findBinary(233, ""))