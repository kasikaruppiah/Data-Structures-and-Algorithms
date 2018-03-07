# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    lr = l
    rl = r
    x = a[lr]
    j = lr
    while (j <= rl):
        if a[j] < x:
            a[lr], a[j] = a[j], a[lr]
            lr += 1
            j += 1
        elif a[j] > x:
            a[j], a[rl] = a[rl], a[j]
            rl -= 1
        else:
            j += 1

    return lr, rl

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    lr, rl = partition3(a, l, r)
    randomized_quick_sort(a, l, lr - 1);
    randomized_quick_sort(a, rl + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
