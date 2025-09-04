def print_squares_table(n):
    max_num = (n ** 2) ** 2
    col_width = len(str(max_num)) + 2

    print(f"{' ':>{col_width}}", end="")
    for i in range(1, n + 1):
        print(f"{i:>{col_width}}", end="")
    print()
    print("-" * (col_width * (n + 1) + 1))

    for i in range(1, n + 1):
        print(f"{i:>{col_width}}|", end="")
        for j in range(1, n + 1):
            print(f"{(i * j) ** 2:>{col_width}}", end="")
        print()

print_squares_table(9)