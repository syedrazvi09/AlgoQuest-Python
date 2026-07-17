def isPalindrome(s):

    # base case / stopping point
    if len(s) == 0 or len(s) == 1:
        return True

    # condition to handle non palindromes
    if s[0] != s[-1]:
        return False

    # recursive call for logic and shrinking problem space
    return isPalindrome(s[1:-1])


print(isPalindrome("racecar"))
