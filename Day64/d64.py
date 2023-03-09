from heapq import heapify, heappush, heappop
from ast import List

# array solution


def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if x != y:
            stones.append(y - x)
    return stones[0] if stones else 0

# heap solution


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapify(stones)
    while len(stones) > 1:
        y = abs(heappop(stones))
        x = abs(heappop(stones))
        if x != y:
            heappush(stones, y-x)
    return abs(stones[0]) if stones else 0
