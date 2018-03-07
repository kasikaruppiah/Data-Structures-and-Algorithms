# Uses python3
import sys

def lcm_naive(a, b):
	for l in range(1, a*b + 1):
		if l % a == 0 and l % b == 0:
			return l

	return a*b

def gcd_effective(a, b):
	if (b == 0):
		return a
	else:
		return gcd_effective(b, a % b)

def lcm_effective(a, b):
	return (a * b) // gcd_effective(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_effective(a, b))

