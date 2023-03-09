import heapq


def KClosest(points, K):
    return sorted(points, key=lambda P: P[0]**2 + P[1]**2)[:K]

# solution using heap
def KClosest(points, K):
    heap = []
    for x, y in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist, x, y))
    return [(x, y) for dist, x, y in heapq.nsmallest(K, heap)]