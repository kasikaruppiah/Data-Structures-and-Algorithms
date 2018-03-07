# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.height = [0] * self.n

    def tree_height(self, vertex):
        parent = self.parent[vertex]
        if parent == -1:
            return 1
        if self.height[vertex]:
            return self.height[vertex]
        self.height[vertex] = 1 + self.tree_height(self.parent[vertex])
        return self.height[vertex]

    def compute_height(self):
        # Replace this code with a faster implementation
        return max([self.tree_height(vertex) for vertex in range(self.n)])


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
