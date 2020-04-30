class RecentCounter:

    def __init__(self):
        self.times = []
        self.minHeapIndex = 0

    def ping(self, t: int) -> int:
        self.times.append(t)
        for i in range(self.minHeapIndex, len(self.times)):
            if(t - 3000 <= self.times[i]):
                self.minHeapIndex = i
                return len(self.times) - self.minHeapIndex

                # Your RecentCounter object will be instantiated and called as such:
                # obj = RecentCounter()
                # param_1 = obj.ping(t)
