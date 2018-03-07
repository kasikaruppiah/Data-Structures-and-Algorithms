#Uses python3

import sys

def get_max_index(a):
    max = a[0]
    index = ø
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
            index = i

    return index

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        amax = get_max_index(a)
        bmax = get_max_index(b)
        res += a[amax] * b[bmax]
        del a[amax]
        del b[bmax]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
