n = int(input())


if 11 <= n % 100 <= 19:
    suffix = 'ов'
elif n % 10 == 1:
    suffix = ''
elif 2 <= n % 10 <= 4:
    suffix = 'а'
else:
    suffix = 'ов'

print(f'{n} программист{suffix}')