class TimeMap:

    def __init__(self):
        self.hashMap = {} # key -> list((times, values))

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        
        self.hashMap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        vals = self.hashMap[key]
        l, r = 0, len(vals) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2

            if vals[m][0] == timestamp:
                return vals[m][1]
            elif vals[m][0] < timestamp:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return "" if vals[res][0] > timestamp else vals[res][1]