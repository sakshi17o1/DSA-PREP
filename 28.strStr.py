def strStr(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1

    for i in range (len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1 
    
# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        ("hello", "ll"),  # expected 2
        ("aaaaa", "bba"), # expected -1
        ("", ""),         # expected 0
        ("abc", "c"),     # expected 2
        ("abc", "d"),     # expected -1
    ]

    for haystack, needle in test_cases:
        result = strStr(None, haystack, needle)
        print(f"haystack='{haystack}', needle='{needle}' -> {result}")

        

