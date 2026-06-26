def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 0:
        return " "

    base = strs[0]
    for i in range(len(base)):
        for words in strs[1:]:
            if (i == len(words) or base[i] != words[i]):
                return base [0:i]
        
    return base

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        ["flower","flow","flight"],  # expected "fl"
        ["dog","racecar","car"],     # expected ""
        ["interstellar", "internet", "internal"],  # expected "inte"
        ["apple", "ape", "april"],   # expected "ap"
        ["single"],                  # expected "single"
    ]

    for strs in test_cases:
        result = longestCommonPrefix(strs)
        print(f"strs={strs} -> {result}")