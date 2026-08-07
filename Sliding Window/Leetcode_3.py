def lols(s):
    seen = set()
    window = 0
    res = 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[window])
            window += 1
        seen.add(s[i])
        res = max(res, i - window + 1)
    return res


s = "1R1T7"
print(lols(s))