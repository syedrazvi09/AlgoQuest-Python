def reverseString(input):
    # base case
    if input == "":
        return ""

    # smallest amount of work in each iteration
    return reverseString(input[1:]) + input[0]


print(reverseString("hello"))