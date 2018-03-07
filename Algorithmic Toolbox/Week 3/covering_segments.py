# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def choose_min_end(segments):
    minEnd = segments[0].end
    for segment in segments:
        if segment.end < minEnd:
            minEnd = segment.end

    return minEnd

def contains_point(segment, end):
    return (segment.start <= end and end <= segment.end)

def optimal_points(segments):
    points = []
    #write your code here
    while(len(segments) > 0):
        minEnd = choose_min_end(segments)
        points.append(minEnd)
        segments[:] = [segment for segment in segments if not contains_point(segment, minEnd)]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
