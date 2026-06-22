def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candy = [1]*n
    for i in range (1,n):
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i - 1] + 1
    
    for i in range (n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]: 
            candy[i] = max(candy[i], candy[i + 1] + 1)   

    return sum(candy)  

# ---- driver code ----
if __name__ == "__main__":
    test_cases = [
        [1, 0, 2],          # expected 5
        [1, 2, 2],          # expected 4
        [1, 3, 4, 5, 2],    # expected 11
    ]

    for ratings in test_cases:
        result = candy(ratings)
        print(f"ratings={ratings} -> {result}")