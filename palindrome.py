def is_palindrome(s):
    cleaned =""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
    # s = "A man, a plan, a canal: Panama"
    # if is_palindrome(s):
    #     print(f'"{s}" is a palindrome.')
    # else:
    #     print(f'"{s}" is not a palindrome.')