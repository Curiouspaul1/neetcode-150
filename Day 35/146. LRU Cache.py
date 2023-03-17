# https://leetcode.com/problems/lru-cache/submissions/917059276/
class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = {} # retains order with fast access
        

    def get(self, key: int) -> int:
        if key in self.order:
            val = self.order[key]
            # move key to the most recently used
            del self.order[key]
            self.order[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check length of storage
        if key in self.order:
            #update order for key to most recently used
            del self.order[key]
            self.order[key] = value
        else:
            if len(self.order) == self.capacity:
                # If we are at capacity we should remove an element before we add 
                # use iterator for quick access of oldest
                to_delete = next(k for k in self.order.keys())
                del self.order[to_delete]
            self.order[key] = value
     


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)