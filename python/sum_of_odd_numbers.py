def row_sum_odd_numbers(n):
    return sum(list(range((n ** 2) - n + 1, (n ** 2) + n, 2)))


if __name__ == "__main__":
    print(row_sum_odd_numbers(13))  # 2197
