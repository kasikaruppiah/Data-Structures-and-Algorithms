# Uses python3
import sys

def get_change(m):
    #write your code here
    c = 0
    for d in (10, 5, 1):
    	c += m // d
    	m %= d

    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
	