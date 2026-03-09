import random

"""
STEP1: Build a Max-Heap from the unsorted array.
STEP2: Repeatedly extract the maximum and place it at the end of the array.
"""

def HeapSort(array):
    n = len(array)

    # STEP1: Build a Max-Heap from the unsorted array.
    for i in range(n // 2 - 1, -1, -1): # heapify starts from the last non-leaf node, all the way up
        _heapify(array, n, i)

    # STEP2: Repeatedly extract the maximum and place it at the end of the array.
    # switch two
    for i in range(n - 1, 0, -1):
        array[0], array[i] = \
        array[i], array[0] # put the element into the last one, ignore it and continue
        _heapify(array, i, 0) # heapify again, and continue the loop

# index: the starting point
# this is a sifting downfunction
def _heapify(array, length, index): # the underscore is to denote that the function is called only in HeapSort()
    largest = index # by default
    left = 2 * index + 1 # get the left child by formula
    right = 2 * index + 2 # get the right child by formula

    # get the largest number among three nodes
    if left < length and array[left] > array[largest]:
        largest = left
    if right < length and array[right] > array[largest]:
        largest = right

    # switch
    if largest != index:
        array[largest], array[index] = \
        array[index], array[largest]
        _heapify(array, length, largest) # continue to sift down

# Test
if __name__ == "__main__":
    array = [random.randint(0, 100) for _ in range(10)]
    print("Before sorting:", array)
    HeapSort(array)
    print("After sorting:", array)

# time complexity: O(nlogn) in all cases, because we have to build the Max-Heap first, which takes O(n), 
# and then we have to extract the maximum n times, which takes O(logn) each time.
# space complexity: O(1) because we are sorting the array in place, and we are not using any extra space.