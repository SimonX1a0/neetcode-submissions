class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        sorted_d = sorted(hm.items(), key=lambda item : item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_d[i][0])
        return res