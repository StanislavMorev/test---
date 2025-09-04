numbers = list(map(int, input().split()))

if len(numbers) == 1:
    print(numbers[0])
else:
    result = []
    n = len(numbers)
    for i in range(n):
        left = numbers[i - 1]
        right = numbers[(i + 1) % n]
        result.append(left + right)
    print(' '.join(map(str, result)))