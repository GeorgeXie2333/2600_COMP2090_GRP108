# Min-Heap & Heap Sort

A self-study implementation of the **Min-Heap** data structure and **Heap Sort** algorithm in Python.

## Files

| File | Description |
|---|---|
| `min_heap_sort.py` | Min-Heap ADT + Heap Sort implementation with demo |

## Data Structure: Min-Heap

An array-based binary tree where every node is ≤ its children, so the root is always the minimum.

**Supported operations:**

| Method | Description | Time |
|---|---|---|
| `insert(val)` | Add a new element | O(log n) |
| `extract_min()` | Remove and return the minimum | O(log n) |
| `peek()` | View the minimum without removing | O(1) |
| `_build_heap(arr)` | Build heap from a list (Floyd's algorithm) | O(n) |

## Algorithm Details & Code

### 1. Min-Heap Operations

The core of the Min-Heap relies on `_sift_up` for insertion and `_sift_down` for extraction or building the heap.

```python
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
```

### 2. Heap Sort Implementation

The Heap Sort algorithm consists of two main steps:
1. **Build a min-heap** from the input array in **O(n)** time using Floyd's algorithm.
2. **Sort the array** by repeatedly swapping the root (minimum element) with the last element of the unsorted section, reducing the heap size, and sifting down the new root. This takes **O(n log n)** time.

**Overall Complexity:** Time O(n log n) | Space O(1) in-place | Stability: Not stable

> **Note:** Since a min-heap always extracts the smallest element first and places it at the end of the shrinking heap, the final array is sorted in **descending order**.

```python
def heap_sort(arr):
    h = MinHeap()
    h._build_heap(arr)

    for i in range(len(h._data) - 1, 0, -1):
        h._swap(0, i)
        h._sift_down(0, i)

    return h._data
```

## Run

```bash
python3 min_heap_sort.py
```

**Example output:**

```
=== MinHeap ADT Demo ===
  insert(5)  ->  heap = [5]
  insert(3)  ->  heap = [3, 5]
  insert(8)  ->  heap = [3, 5, 8]
  insert(1)  ->  heap = [1, 3, 8, 5]
  insert(4)  ->  heap = [1, 3, 8, 5, 4]

  peek()        ->  1
  extract_min() ->  1,  heap = [3, 4, 8, 5]
  extract_min() ->  3,  heap = [4, 5, 8]

=== Heap Sort Demo ===
  Input:  [9, 4, 7, 2, 6, 1, 8, 3, 5]
  Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
```
