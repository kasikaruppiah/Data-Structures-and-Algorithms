# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_pisano_length(m):
    previous = 0
    current = 1
    for _ in range(m ** 2 + 1):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return _ + 1

def get_fibonacci_huge_effective(n, m):
    if n <= 1:
        return n

    pisano = [0, 1]
    previous = 0
    current = 1
    pisano_limit = get_pisano_length(m)
    pisano_index = n % pisano_limit
    if (pisano_index > 1):
        for _ in range(2, pisano_index + 1):
            previous, current = current, (previous + current) % m
            pisano.append(current)

    return pisano[pisano_index]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_effective(n, m))
