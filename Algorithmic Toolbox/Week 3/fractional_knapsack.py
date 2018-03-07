# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	# write your code here
	if capacity == 0:
		return value

	for i in range(len(weights)):
		wi = -1
		max = 0
		for j in range(len(weights)):
			if weights[j] > 0 and values[j] / weights[j] > max:
				max = values[j] / weights[j]
				wi = j

		if wi > -1:
			weight = min(weights[wi], capacity)
			capacity -= weight
			value += weight * max
			weights[wi] -= weight 	

	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
