from collections import Counter

def first_non_repeating_char(s):
    char_count = Counter(s)
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))  # Output: "w"
print(first_non_repeating_char("aabbcc"))  # Output: None