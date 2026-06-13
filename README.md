# Data Structures & Systems Design Assignment

## Problem 1: LRU Cache

I implemented LRU Cache using a HashMap and Doubly Linked List.

- HashMap provides O(1) access to nodes
- Doubly Linked List maintains usage order
- Most recently used items are moved to front
- Least recently used items are removed when capacity is full

This ensures O(1) time complexity for both get and put operations.

---

## Problem 2: Event Scheduler

### can_attend_all
Checks if events overlap after sorting by start time.

### min_rooms_required
Uses a min-heap to track ongoing meetings and calculate minimum rooms required.

---

## Time Complexity
- LRU Cache: O(1) for get and put
- can_attend_all: O(n log n)
- min_rooms_required: O(n log n)

---

## Author
Assignment submission for Software Engineering Intern role
