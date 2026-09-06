class TimeMap:

    def __init__(self):
        self.hashtable = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashtable[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashtable:
            return ''
        if timestamp < self.hashtable[key][0][0]:
            return ''
        if self.hashtable[key][-1][0] < timestamp:
            return self.hashtable[key][-1][1]
        
        data = self.hashtable[key]
        l = 0
        r = len(data) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if data[m][0] < timestamp:
                l = m + 1
            elif data[m][0] > timestamp:
                r = m - 1
            else:
                return data[m][1]
        
        return data[r][1]