def evaluateRPN(tokens):

    stack = []
    ops = {'+', '-', '*', '/'}

    for tok in tokens:
        if tok in ops:
            b = stack.pop()
            a = stack.pop()
            if tok == '+':
                stack.append(a + b)
            if tok == '-':
                stack.append(a - b)
            if tok == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack.pop()


tokens = [2, 5, '+', 1, '/', 3, '*', 4]
print(evaluateRPN(tokens))