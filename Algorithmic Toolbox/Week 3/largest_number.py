#Uses python3

import sys

def get_max_number(a):
	max = a[0]
	for n in a:
		if int(str(max) + str(n)) < int(str(n) + str(max)):
			max = n

	return max


def largest_number(a):
	#write your code here
	res = ""
	for i in range(len(a)):
		maxNum = get_max_number(a)
		res += maxNum
		a.remove(maxNum)

	return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
