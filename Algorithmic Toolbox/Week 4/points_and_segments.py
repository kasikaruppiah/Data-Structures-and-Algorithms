# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))
    sorted_points = sorted(chain(start_points, end_points, point_points), key=lambda a: (a[0], a[1]))
    segment = 0

    for num, identifier, index in sorted_points:
        if identifier == 'l':
            segment += 1
        elif identifier == 'r':
            segment -= 1
        else:
            cnt[index] = segment

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
