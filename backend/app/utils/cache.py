class Cache:
    def __init__(self):
        self.store = {}
    def get(self, key):
        return self.store.get(key)
