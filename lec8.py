def palindrome_string(s):
    is_palindrome = False
    si = 0
    ei = len(s) - 1

    while si < ei:
        if s[si] == s[ei]:
            is_palindrome = True

        si += 1
        ei -= 1

    return is_palindrome

