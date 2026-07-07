def reverseWords(self, s: str) -> str:
    s = s.strip()
    words = s.split()
    words.reverse()
    result = " " .join(words)
    return result

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        "the sky is blue",          # expected "blue is sky the"
        "  hello world  ",          # expected "world hello"
        "a good   example",         # expected "example good a"
        "  Bob    Loves  Alice   ", # expected "Alice Loves Bob"
        "Alice does not even like bob", # expected "bob like even not does Alice"
    ]

    for s in test_cases:
        result = reverseWords(None, s)
        print(f"s='{s}' -> '{result}'")