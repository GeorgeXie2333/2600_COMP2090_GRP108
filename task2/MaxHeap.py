class MaxHeap:
    def __init__(self):
        self.heap = []

    def _heapify_down(self, index): # index: the node to be sifted down
        size = len(self.heap)
        largest = index # assume the largest number is at index now
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = \
            self.heap[index], self.heap[largest]
            # continue all the way down
            self._heapify_down(largest)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = \
            self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # swap the root to the last one
        if len(self.heap) == 0:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # pop it out
        max_val = self.heap.pop()
        # restore the MaxHeap
        self._heapify_down(0)
        return max_val
    
    def build_heap(self, array):
        self.heap = array[:] # copy one to avoid changing the original array
        start = len(self.heap) // 2 - 1
        for i in range(start, -1, -1):
            self._heapify_down(i)