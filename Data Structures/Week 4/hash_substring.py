# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(s, p, m):
	h = 0
	for c in reversed(s):
		h = (h * m + ord(c)) % p
	return h

def precompute_hash(text, len_pattern, p, m):
    H = [None] * (len(text) - len_pattern + 1)
    S = text[len(text) - len_pattern:]
    H[len(text) - len_pattern] = PolyHash(S, p, m)
    y = 1
    for i in range(len_pattern):
        y = (y * m) % p
    for i in range(len(text) - len_pattern - 1, -1, -1):
        H[i] = (m * H[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern])) % p
    return H

def get_occurrences(pattern, text):
	result = []
	p = 1610612741
	m = 263
	h = PolyHash(pattern, p, m)
	H = precompute_hash(text, len(pattern), p, m)

	for i in range(len(text) - len(pattern) + 1):
		if h == H[i] and text[i : i + len(pattern)] == pattern:
			result.append(i)

	return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

