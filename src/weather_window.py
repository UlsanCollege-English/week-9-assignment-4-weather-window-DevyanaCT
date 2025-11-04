import heapq

"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""

def sliding_window_max(nums, k):
    # Edge cases
    if not nums or k <= 0:
        return []
    if k > len(nums):
        k = len(nums)

    result = []
    heap = []  # will store (-value, index)

    for i, val in enumerate(nums):
        # Push current value with negative sign to simulate max-heap
        heapq.heappush(heap, (-val, i))

        # Remove elements from heap that are out of current window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Once the first full window is reached, record max
        if i >= k - 1:
            result.append(-heap[0][0])  # convert back to positive

    return result
