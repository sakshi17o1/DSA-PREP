def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0
    left_max, right_max = height[l], height[r]

    while l < r:
        if left_max <= right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]

    return res

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],   # expected 6
        [4, 2, 0, 3, 2, 5],                     # expected 9
        [1, 0, 2],                              # expected 1
    ]

    for height in test_cases:
        result = trap(height)
        print(f"height={height} -> {result}")