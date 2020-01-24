# Heaps

- Heaps are specialized binary tree.
- It's a complete binary tree.
- Heap property: Key at each node is at least greater than it's children.

### Max-Heap and Min-Heap: 
- O(logn): insertion
- O(1): get max element
- O(logn): deletion for max-element
- O(n): searching for an arbitrary keys

### When to use heap?
- When all you care about smallest or largest elements 
- and when you do not need to support fast lookup, delete or search operations.
- Heap is a good choice for k largest or k smallest elements in a collectioin.
- For K-largest, use min-heap.
- For K-smallest, use max-heap.
