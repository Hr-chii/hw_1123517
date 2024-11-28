#Your Name:Callie
#Student ID:1123517
#Date of Submission:2024/11/28

import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))

    return result

# Example Input
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print("Merged Array:", merge_k_sorted_arrays(arrays))  # Output: Merged Array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
