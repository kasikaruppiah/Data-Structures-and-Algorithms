# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    steps = [0]

    for i in range(1, n + 1):
        steps.append(steps[i - 1])
        if (i % 2 == 0):
            steps[i] = min(steps[i], steps[i // 2])
        if (i % 3 == 0):
            steps[i] = min(steps[i], steps[i // 3])
        steps[i] += 1

    step = n
    while (step > 0):
        sequence.append(step)
        if (steps[step] - 1 == steps[step - 1] - 1 + 1):
            step -= 1
        elif (step % 2 == 0 and steps[step] - 1 == steps[step // 2] - 1 + 1):
            step //= 2
        else:
            step //= 3

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
