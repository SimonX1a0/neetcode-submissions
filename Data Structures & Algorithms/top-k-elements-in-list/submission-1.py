class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        

        heap = []
        for key, val in hm.items():
            heapq.heappush(heap, (-val, key))
        res = []
        for i in range(k):
            element = heapq.heappop(heap)
            res.append(element[1])
        return res