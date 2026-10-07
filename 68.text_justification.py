class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, length =[], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words [i]) > maxWidth:
                # line complete 
                extra_space = maxWidth - length 
                spaces = extra_space // max (1, len(line) - 1)
                remainder = extra_space % max (1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line [j] += " " * spaces
                    if remainder :
                        line[j] +=  " "
                        remainder -= 1
                res.append ("".join (line))
                line, length = [], 0  # Reset line and length 

            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handling last line 

        last_line = " " . join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res

# ---- driver code ----
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (["Science","is","what","we","understand","well","enough","to","explain",
          "to","a","computer.","Art","is","everything","else","we","do"], 20),
    ]

    for words, maxWidth in test_cases:
        result = solution.fullJustify(words, maxWidth)
        print(f"words={words}, maxWidth={maxWidth} -> {result}")

    