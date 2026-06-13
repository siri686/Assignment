import heapq
def can_attend_all(events):
    if not events:
        return True

    # sort by start time
    events.sort(key=lambda x: x[0])

    for i in range(1, len(events)):
        prev_end = events[i - 1][1]
        curr_start = events[i][0]

        if curr_start < prev_end:
            return False

    return True

def min_rooms_required(events):
    if not events:
        return 0

    # sort by start time
    events.sort(key=lambda x: x[0])

    min_heap = []

    for start, end in events:
        # free up rooms that are finished
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

    return len(min_heap)


# Testing
events1 = [(9, 10), (10, 11), (11, 12)]
events2 = [(9, 12), (10, 11), (11, 13)]

print(can_attend_all(events1))  # True
print(can_attend_all(events2))  # False

print(min_rooms_required(events1))  # 1
print(min_rooms_required(events2))  # 2