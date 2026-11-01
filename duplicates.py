from collections import Counter

def is_duplicate(s):
    count = Counter(s)
    return [n for n, c in count.items() if c > 1]

print(is_duplicate([1, 2, 3, 2, 4, 3, 3]))  # Output: [2, 3]