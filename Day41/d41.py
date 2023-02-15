class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1

        return self.cache[key]
        

    def put(self, key, value):

        if key in self.cache:
            self.cache[key] = value
        else:
            self.cache[key] = value
        if len(self.cache) >= self.capacity:
            keys = list(self.cache.keys)
            del self.cache[keys[0]]
