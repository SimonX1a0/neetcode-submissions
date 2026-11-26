class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in hm:
                return [hm[num], i]
            hm[diff] = i
        