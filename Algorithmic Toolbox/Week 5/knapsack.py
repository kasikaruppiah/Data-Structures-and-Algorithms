# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    K = [[0 for j in range(len(w) + 1)] for n in range(W + 1)]

    for j in range(1, len(w) + 1):
    	for n in range(1, W + 1):
        	if (w[j - 1] > n):
        		K[n][j] = K[n][j - 1]
        	else:
        		K[n][j] = max(K[n][j - 1], K[n - w[j - 1]][j - 1] + w[j - 1])

    return K[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
