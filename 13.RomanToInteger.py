def romanToInt( s: str) -> int:
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    res = 0

    for i in range (len(s)):
        if (i + 1 < len(s) and dic[s[i]] < dic[s[i+1]]) :
            res -= dic[s[i]]
        else:
            res += dic[s[i]]
    return res

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        "III",      # expected 3
        "LVIII",    # expected 58
        "MCMXCIV",  # expected 1994
    ]

    for s in test_cases:
        result = romanToInt(s)
        print(f"s={s} -> {result}")