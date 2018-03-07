# Uses python3
import random

def MaxPairwiseProduct(a):
	n = len(a)
	result = 0
	for i in range(0, n):
		for j in range(i + 1, n):
			if (a[i] * a[j] > result):
				result = a[i] * a[j]

	return result

def MaxPairwiseProductFast(a):
	n = len(a)
	max1 = -1
	for i in range(0, n):
		if (max1 == -1 or a[i] > a[max1]):
			max1 = i

	max2 = -1
	for i in range(0, n):
		if (i != max1 and (max2 == -1 or a[i] > a[max2])):
			max2 = i
	# print("{0} {1}".format(max1, max2))

	return a[max1] * a[max2]

def StressTest():
	while (True):
		n = random.randint(2, 1001)
		print(n)
		a = []
		for i in range(0, n):
			a.append(random.randint(0, 99999))
		print(' '.join(map(str, a)))

		result1 = MaxPairwiseProduct(a)
		result2 = MaxPairwiseProductFast(a)
		if (result1 != result2):
			print("Wrong answer: {0} {1}".format(result1, result2))
			break
		else:
			print("OK")

# StressTest()
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = MaxPairwiseProductFast(a)
print(result)