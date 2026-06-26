def lengthOfLastWord(self, s: str) -> int:
    i, length = len (s) - 1, 0
    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        "Hello World",          # expected 5
        "   fly me   to   the moon  ",  # expected 4
        "luffy is still joyboy",         # expected 6
    ]

    for s in test_cases:
        result = lengthOfLastWord(None, s)
        print(f"s={s} -> {result}")