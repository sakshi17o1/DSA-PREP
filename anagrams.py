from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False