# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    self.n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self.n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def sift_down(self, i):
    minIndex = i
    l = 2 * i + 1
    if l < self.n and self._data[l] < self._data[minIndex]:
      minIndex = l
    r = 2 * i + 2
    if r < self.n and self._data[r] < self._data[minIndex]:
      minIndex = r
    if i != minIndex:
      self._swaps.append((i, minIndex))
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self.sift_down(minIndex)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(self.n // 2, -1, -1):
      self.sift_down(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
