class MinHeap:
    """Min-Heap using a list-based binary tree."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i):
        # Move node up while smaller than its parent
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] < self._data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i, size):
        # Move node down to restore heap property
        while True:
            smallest, left, right = i, 2*i+1, 2*i+2
            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def insert(self, val):
        """O(log n) — append then sift up."""
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def extract_min(self):
        """O(log n) — swap root with last, pop, then sift down."""
        if not self._data:
            raise IndexError("heap is empty")
        self._swap(0, len(self._data) - 1)
        val = self._data.pop()
        if self._data:
            self._sift_down(0, len(self._data))
        return val

    def peek(self):
        """O(1) — return minimum without removing."""
        if not self._data:
            raise IndexError("heap is empty")
        return self._data[0]

    def _build_heap(self, arr):
        """O(n) — Floyd's algorithm: sift down from last non-leaf."""
        self._data = arr[:]
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i, len(self._data))


def heap_sort(arr):
    """
    Heap Sort using a min-heap.
    Time: O(n log n)  |  Space: O(1) in-place  |  Stable: No

    1. Build min-heap in O(n).
    2. Swap root (min) with last element, shrink heap, sift down.
       Repeating this accumulates elements largest-to-smallest at the end,
       resulting in descending order in-place.
    """
    h = MinHeap()
    h._build_heap(arr)

    for i in range(len(h._data) - 1, 0, -1):
        h._swap(0, i)
        h._sift_down(0, i)

    return h._data


if __name__ == "__main__":
    print("=== MinHeap ADT Demo ===")
    heap = MinHeap()
    for v in [5, 3, 8, 1, 4]:
        heap.insert(v)
        print(f"  insert({v})  ->  heap = {heap._data}")

    print(f"\n  peek()        ->  {heap.peek()}")
    print(f"  extract_min() ->  {heap.extract_min()},  heap = {heap._data}")
    print(f"  extract_min() ->  {heap.extract_min()},  heap = {heap._data}")

    print("\n=== Heap Sort Demo ===")
    data = [9, 4, 7, 2, 6, 1, 8, 3, 5]
    print(f"  Input:  {data}")
    print(f"  Output: {heap_sort(data)}")
