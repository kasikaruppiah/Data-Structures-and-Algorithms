# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

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

def fibonacci_sum_effective(n):
    return (get_fibonacci_huge_effective(n + 2, 10) - 1) % 10

def fibonacci_partial_sum_effective(from_, to):
    return (fibonacci_sum_effective(to) - fibonacci_sum_effective(from_)) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_effective(from_ - 1, to))