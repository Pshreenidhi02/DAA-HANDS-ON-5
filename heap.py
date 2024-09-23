from typing import TypeVar, List, Generic

T = TypeVar('T')

class MinHeap(Generic[T]):
    
    def __init__(self, arr: List[T] = None) -> None:
        # Initialize the heap from an array if provided, else an empty list
        self.heap: List[T] = arr if arr else []
        if arr:
            self.build_min_heap()

    def parent(self, i: int) -> int:
        # Returns index of the parent using bit manipulation (i-1) // 2
        return (i - 1) >> 1

    def left(self, i: int) -> int:
        # Returns index of the left child using bit manipulation 2*i + 1
        return (i << 1) + 1

    def right(self, i: int) -> int:
        # Returns index of the right child using bit manipulation 2*i + 2
        return (i << 1) + 2

    def build_min_heap(self) -> None:
        # Build a min heap by heapifying from the last parent node down to the root
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(n, i)

    def heapify(self, n: int, i: int) -> None:
        # Ensure that the subtree rooted at index i maintains the heap property
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(n, smallest)

    def insert(self, value: T) -> None:
        # Insert a new element into the heap
        self.heap.append(value)
        i = len(self.heap) - 1
        parent = self.parent(i)

        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent(i)

    def pop(self) -> T:
        # Remove and return the root element (smallest), then restore heap property
        if not self.heap:
            return None

        # Replace root with the last element and pop the last element
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Re-heapify the new root
        self.heapify(len(self.heap), 0)
        return root

    def get_root(self) -> T:
        # Return the root element (smallest) without removing it
        return self.heap[0] if self.heap else None

    def __str__(self) -> str:
        # String representation for easy visualization of the heap
        return str(self.heap)

# Example usage of the MinHeap
if __name__ == "__main__":
    
    # Example 1: Using a list of integers
    arr1 = [30, 20, 50, 40, 10, 60]
    print("Initial array:", arr1)
    heap1 = MinHeap(arr1)
    print("Min Heap (after build_min_heap):", heap1)

    # Insert a new element into the heap
    heap1.insert(5)
    print("Heap after inserting 5:", heap1)

    # Pop the root (min element)
    print("Popped root element:", heap1.pop())
    print("Heap after popping root:", heap1)

    # Example 2: Using a list of floats
    arr2 = [5.5, 2.1, 9.8, 7.4, 1.3, 4.2]
    print("\nInitial float array:", arr2)
    heap2 = MinHeap(arr2)
    print("Min Heap (after build_min_heap):", heap2)

    # Insert a new element into the float heap
    heap2.insert(3.6)
    print("Heap after inserting 3.6:", heap2)

    # Pop the root from the float heap
    print("Popped root element:", heap2.pop())
    print("Heap after popping root:", heap2)

    # Example 3: Using a list of custom data (tuples)
    arr3 = [(3, 'C'), (2, 'B'), (5, 'E'), (1, 'A')]
    print("\nInitial tuple array:", arr3)
    heap3 = MinHeap(arr3)
    print("Min Heap (after build_min_heap):", heap3)

    # Insert a new tuple
    heap3.insert((0, 'Z'))
    print("Heap after inserting (0, 'Z'):", heap3)

    # Pop the root (smallest tuple)
    print("Popped root element:", heap3.pop())
    print("Heap after popping root:", heap3)
