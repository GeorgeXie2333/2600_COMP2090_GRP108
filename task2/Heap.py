from MaxHeap import MaxHeap
from MinHeap import MinHeap
class Heap:
    def __init__(self, max_or_min):
        if max_or_min.lower() == "min":
            self.Heap = self.MinHeap()
        elif max_or_min.lower() == "max":
            self.Heap = self.MaxHeap()