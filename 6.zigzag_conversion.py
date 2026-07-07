def convert(s: str, numRows: int) -> str:

    if numRows == 1 or numRows >= len(s):
        return s

    t = list(range(numRows)) + list(range(numRows - 2, 0, -1))

    r = [''] * numRows

    for i, char in enumerate(s):
        r[t[i % len(t)]] += char

    return ''.join(r)

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        ("PAYPALISHIRING", 3),  # expected "PAHNAPLSIIGYIR"
        ("PAYPALISHIRING", 4),  # expected "PINALSIGYAHRPI"
        ("A", 1),               # expected "A"
        ("ABCD", 2),            # expected "ACBD"
        ("HELLOZIGZAG", 5),     # expected "HLOEZGILAG"
    ]

    for s, numRows in test_cases:
        result = convert(s, numRows)
        print(f"s={s}, numRows={numRows} -> {result}")