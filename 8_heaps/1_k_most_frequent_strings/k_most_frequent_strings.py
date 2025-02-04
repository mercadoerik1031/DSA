"""
https://leetcode.com/problems/top-k-frequent-words/description/

Find the k most frequently occurring strings in an array, and return them sorted by frequency,
in descending order. If two strings have the same frequency, sort them in lexicographical order.

Example:
    Input: strs = ["go", "coding", "byte", "byte", "go", "interview", "go"], k = 2
    Output: ["go", "byte"]

Explanation:
    The strings "go" and "byte" appear the most frequently, with frequencies of 3 and 2 respectively

Constraints:
    k <= n, where n denotes the length of the array
"""


import heapq
from typing import List


class Pair:
    def __init__(self: object, string: str, freq: int) -> None:
        self.string = string
        self.freq = freq

    def __lt__(self: object, other: object) -> bool:
        if self.freq == other.freq:
            return self.string > other.string

        return self.freq < other.freq


def k_most_frequent_strs(strs: List[str], k: int) -> List[str]:
    frequencies = {}
    for word in strs:
        frequencies[word] = frequencies.get(word, 0) + 1

    heap = []

    for word, count in frequencies.items():
        heapq.heappush(heap, Pair(word, count))

        if len(heap) > k:
            heapq.heappop(heap)

    return [heapq.heappop(heap).string for _ in range(k)][::-1]


# Time Complexity: O(n + k log(n)), Space Complexity: O(n)
